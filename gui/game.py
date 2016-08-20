# encoding=utf-8


# ------ Imports ------

import pygame
import os
import inspect

from copy import copy
import constants as cst
from isometric import isoutils
from . import misc, menu
from entities import turretlist

map_center = isoutils.iso_to_cart((cst.SCREEN_WIDTH//2, cst.SCREEN_HEIGHT//2))
number_to_turret = {
    None: lambda: turretlist.BasicSmall(),
    0: lambda: turretlist.BasicSmall(),
    1: lambda: turretlist.BasicLarge(),
    2: lambda: turretlist.MissileSmall(),
    3: lambda: turretlist.MissileLarge(),
}

class Score:
    def __init__(self, msg, pos, value=0, color = cst.RED):
        self.msg = menu.Message(msg, pos, color = color, center = False)
        self.l = self.msg.rect.right + 5

        self.val = value
        self.val_msg = menu.Message(str(value), pos, color = color, center = False)
        self.val_msg.rect.left = self.l

        self.pos = pos

    def update(self, val=None):
        if val is not None and val != self.val :
            self.val_msg.changeMessage(str(val))


    def display(self, screen = pygame.display.get_surface()):
        self.val_msg.display(screen)
        self.msg.display(screen)


class TurretBar:
    ''' La barre de selection des tourelles en haut de l'écran'''

    def __init__(self):
        self.bgimg, self.bgrect = misc.load_image("gui","bar.png")
        self.turrets = pygame.sprite.Group()
        turret_names, turret_classes = zip(*inspect.getmembers(turretlist, inspect.isclass))
        # fetch distinct turret types
        turret_types = []
        for name in turret_names:
            short = name.replace("Small", "").replace("Large", "")
            if short not in turret_types:
                turret_types.append(short)
        # add turrets of each type and size
        for i, typ in enumerate(turret_types):
            if typ+"Small" in turret_names:
                self.turrets.add(
                    TurretButton(
                        name=typ,
                        class_maker=turret_classes[turret_names.index(typ+"Small")],
                        large=False,
                        center=(48*(i+1), 32)
                    )
                )
            if typ+"Large" in turret_names:
                self.turrets.add(
                    TurretButton(
                        name=typ,
                        class_maker=turret_classes[turret_names.index(typ+"Large")],
                        large=True,
                        center=(48*(i+1), 64)
                    )
                )
        self.bgrect.topleft = (0, 0)

    def update(self, mouse_event, click_event):
        selected_turret = None
        if click_event is not None:
            for t in self.turrets:
                t.selected = False
            self.turrets.update(mouse_event, click_event)
            for t in self.turrets:
                if t.selected:
                    selected_turret = t.instanciate()
        else:
            self.turrets.update(mouse_event, click_event)
        return selected_turret

    def display(self, screen):
        screen.blit(self.bgimg, self.bgrect)
        for t in self.turrets:
            t.display(screen)


class DescriptionWindow:
    """
    A small window that displays every information about a turret. Linked to a TurretButton class.
    DescriptionWindow(self, datas) -> DescriptionWindow
        datas = a dict containing entries "preview","title","descr","price", "large"
    """
    def __init__(self, datas):
        self.bg, self.bg_rect = misc.load_image("gui","desc.png")
        self.bg_rect.topleft = (2, 102)
        self.dict = datas
        self.toblit = []

        # add the preview to blit
        preview, preview_rect = self.dict["preview"]
        preview_rect.topleft = (8, 108)
        self.toblit.append((preview, preview_rect))
        # add the title to blit
        title = cst.GUI_TITLE_FONT.render(self.dict["title"], True, cst.PAPER)
        title_rect = title.get_rect()
        title_rect.topleft = (50, 108)
        self.toblit.append((title, title_rect))
        # add the price to blit
        price = cst.GUI_DESCR_FONT.render("Price : " + self.dict["price"], True, cst.PAPER)
        price_rect = price.get_rect()
        price_rect.topleft = (8, 150)
        self.toblit.append((price, price_rect))
        # add size to blit
        if self.dict["large"]:
            large = cst.GUI_DESCR_FONT.render("Size : Large", True, cst.PAPER)
        else:
            large = cst.GUI_DESCR_FONT.render("TSize : Small", True, cst.PAPER)
        large_rect = large.get_rect()
        large_rect.topleft = (8,170)
        self.toblit.append((large, large_rect))
        # add description
        descr = cst.GUI_DESCR_FONT.render(self.dict["descr"], True, cst.PAPER)
        descr_rect = descr.get_rect()
        descr_rect.topleft = (8,190)
        self.toblit.append((descr, descr_rect))

    def display(self,screen = pygame.display.get_surface()):
        screen.blit(self.bg, self.bg_rect)
        for image, rect in self.toblit:
            screen.blit(image, rect)



class TurretButton(pygame.sprite.Sprite):
    '''Bouton de selection d'une tourelle dans la GUI '''

    def __init__(self, name="", class_maker=None, large=False, **kwargs):
        pygame.sprite.Sprite.__init__(self)

        self.instanciate = class_maker  # a function that instanciates real turrets

        self.preview, self.rect =  misc.load_image("turrets", "test{}.png".format("_large" if large else ""))
        for key, val in kwargs.items():
            setattr(self.rect, key, val)
        
        self.title = name
        self.price = "100"
        self.descr = "This is a {}".format(name)

        d = {
            "title": self.title, 
            "price": self.price,
            "descr": self.descr,
            "large": large,
            "preview": (copy(self.preview), copy(self.rect)),
        }
        self.description_window = DescriptionWindow(d)

        self.hover = False
        self.selected = False

    def update(self, mouse_event, click_event):
        if mouse_event is not None:
            pos = mouse_event.pos
            if not self.hover:
                if self.rect.collidepoint(pos):
                    self.hover = True
            else:
                if not self.rect.collidepoint(pos):
                    self.hover = False
        if click_event is not None and click_event.button == 1:
            pos = click_event.pos
            if not self.selected:
                if self.rect.collidepoint(pos):
                    self.selected = True
            else:
                if self.rect.collidepoint(pos):
                    self.selected = False

    def display(self, screen):
        screen.blit(self.preview, self.rect)
        if self.hover:
            self.description_window.display(screen)
        if self.selected:
            misc.draw_frame(screen, self.rect, cst.YELLOW)


class GUI:
    """
    The class that deals with the GUI of the game.
    Handles the top turret selector, the score, and various buttons
    """

    def __init__(self):
        self.turret_bar = TurretBar()
        self.score = 0
        self.money = 400
        self.wave = 0
        self.selected_turret = None  # turret bound to mouse
        self.undertile = None  # tile under selected_turret

        self.next_wave = menu.Button("Next Wave", (0, 0), font=cst.TEXT_FONT, color=cst.RED)
        self.next_wave.rect.bottomright = (1270, 710)

        self.disp_score = Score("Score :", (10, 610), self.score)
        self.money_score = Score("Money :", (10, 640), self.money)
        self.wave_score = Score("Wave  :", (10, 670), self.wave)

    def update(self, mouse_event, mouse_click):
        # place current selected turret if click
        placed_turret = None
        if self.selected_turret is not None and mouse_click is not None:
                placed_turret, self.selected_turret = self.selected_turret, None
        # assign new selected after update of turret_bar
        selected_turret = self.turret_bar.update(mouse_event, mouse_click)
        if selected_turret is not None and mouse_click is not None:
            self.selected_turret = selected_turret
            self.selected_turret.iso_pos = mouse_click.pos
            self.selected_turret.update()
        # move current selected turret with the mouse and report a turret is being placed
        if self.selected_turret is not None:
            placed_turret = "placing"
            if mouse_event is not None:
                self.selected_turret.iso_pos = mouse_event.pos
        self.next_wave.update(mouse_event, mouse_click)
        return {"placed_turret": placed_turret}

    def display(self, screen):
        self.turret_bar.display(screen)
        self.next_wave.display(screen)
        self.disp_score.display(screen)
        self.money_score.display(screen)
        self.wave_score.display(screen)
        if self.selected_turret is not None:
            if self.undertile is not None:
                pygame.draw.polygon(screen, cst.PAPER, [self.undertile.iso_rect.midbottom, self.undertile.iso_rect.midleft, self.undertile.iso_rect.midtop, self.undertile.iso_rect.midright], 1)
            self.selected_turret.display(screen)


class Cursor:
    """
    A textual cursor which will follow the mouse's moves.
    """
    def __init__(self, parent):
        self.pos = (0, 0)
        self.parent = parent
        self.cursor_image, self.cursor_rect = load_image("cursor.png")
        self.selected = None
        self.image, self.rect = self.cursor_image, self.cursor_rect

    def select(self, obj=None):
        if obj is None:
            self.selected = None
            self.image, self.rect = self.cursor_image, self.cursor_rect
        else:
            self.selected = obj
            self.image, self.rect = load_image(self.selected.preview)

    def update(self, mouse_event, click_event):
        """
        Updates the cursor's state, especially brings it to the position of the mouse.
        """
        x, y = mouse_event.pos
        self.rect.topleft = ((x//10)*10, (y//10)*10)
        if x + self.rect.width < 601 and x > self.rect.width//2:
            self.parent.blit(self.image, self.rect)

    def display(self, screen):
        screen.blit(self.image, self.rect)
