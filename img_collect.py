# Module for draw functions
import pygame as pg


pg.init()


class Collection:
    def __init__( self ):
        # List for all objects and sprites
        self.list = [ ]

    def add( self, instance ):
        self.list.append( instance )

    def combine( self, group ):
        self.list.extend( group )

    def run( self ):
        for item in self.list:
            if ( item.DEPENDENCE == True ):
                item.run()


    def draw( self, surface):
        for item in self.list:
            item.draw( surface )


class EnemyCollection:
    def __init__( self ):
        # List for all objects and sprites
        self.list = [ ]

    def add( self, instance ):
        self.list.append( instance )

    def combine( self, group ):
        self.list.extend( group )

    def run( self, boid, target ):
        for item in self.list:
            if ( item.DEPENDENCE == True ):
                item.run( boid, target )


    def draw( self, surface):
        for item in self.list:
            item.draw( surface )
