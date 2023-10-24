def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(assets.image("""
        shot
    """), Spaceplane, 200, 0)
    animation.run_image_animation(projectile,
        [img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                        . . 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . 3 3 3 3 3 3 3 3 3 3 3 3 . . 
                        . . 2 2 2 2 2 2 2 2 2 2 2 2 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . 2 2 2 2 . . . 
                        . . . . . . . 2 2 1 1 1 1 2 . . 
                        . . . . 2 2 3 3 1 1 1 1 1 1 . . 
                        . . 3 3 3 3 1 1 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . 3 3 2 2 3 1 1 1 1 1 1 1 . . 
                        . . . . . . 2 2 3 1 1 1 1 2 . . 
                        . . . . . . . . . 2 2 2 2 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . 1 1 3 . . . . . . 
                        . . . . . . 1 3 . 3 3 . . . . . 
                        . . . . . . 1 . . . 3 2 2 3 . . 
                        . . . . . 1 3 . . . 2 2 1 3 3 . 
                        . . . . . 1 3 . 2 2 3 1 1 1 3 . 
                        . . 2 2 2 1 3 3 3 3 3 1 1 1 3 . 
                        . . 1 1 1 1 3 1 1 1 1 1 1 1 3 . 
                        . . 2 2 2 1 3 3 3 3 3 1 1 1 3 . 
                        . . . . . 1 3 . 2 2 3 1 1 1 3 . 
                        . . . . . 1 3 . . . 2 2 1 3 3 . 
                        . . . . . . 1 . . . 3 2 2 3 . . 
                        . . . . . . 1 3 . 3 3 . . . . . 
                        . . . . . . . 1 1 3 . . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . 3 3 . . . 3 . . . . . 
                        . . . . 3 3 . . . . 3 3 . . . . 
                        . . . . 3 . . . . . . 3 3 . . . 
                        . . . . . . . . . . . . 3 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . 3 . . . . . . . . . . . . . 
                        . . 3 . . . . . . . . . . 3 . . 
                        . . 3 . . . . . . . . . . 3 . . 
                        . . . . . . . . . . . . . 3 . . 
                        . . . . . . . . . . . . . . . . 
                        . . . 3 . . . . . . . . . . . . 
                        . . . 3 3 . . . . . . 3 . . . . 
                        . . . . 3 3 . . . . 3 3 . . . . 
                        . . . . . . . . . 3 3 . . . . . 
                        . . . . . . . . . . . . . . . .
            """),
            img("""
                . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . 2 2 2 2 . . . 
                        . . . . . . . 2 2 1 1 1 1 2 . . 
                        . . . . 2 2 3 3 1 1 1 1 1 1 . . 
                        . . 3 3 3 3 1 1 1 1 1 1 1 1 . . 
                        . . 1 1 1 1 1 1 1 1 1 1 1 1 . . 
                        . . 3 3 2 2 3 1 1 1 1 1 1 1 . . 
                        . . . . . . 2 2 3 1 1 1 1 2 . . 
                        . . . . . . . . . 2 2 2 2 . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . . 
                        . . . . . . . . . . . . . . . .
            """)],
        40,
        False)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_life_zero():
    game.game_over(False)
info.on_life_zero(on_life_zero)

def on_on_score():
    game.game_over(True)
info.on_score(50, on_on_score)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(otherSprite, effects.fire, 150)
    scene.camera_shake(2, 500)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    otherSprite2.destroy()
    info.change_life_by(-1)
    scene.camera_shake(4, 500)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bogey: Sprite = None
projectile: Sprite = None
Spaceplane: Sprite = None
scene.set_background_image(assets.image("""
    background
"""))
Spaceplane = sprites.create(assets.image("""
    player
"""), SpriteKind.player)
controller.move_sprite(Spaceplane, 100, 100)
Spaceplane.set_stay_in_screen(True)
info.set_life(3)
info.set_score(0)
game.splash("are you ready?")
music.play(music.create_song(hex("""
        0078000408010105001c000f0a006400f4010a00000400000000000000000000000000000000022c0004000800012708000c0002252a0c001000012710001400012514001800012918001c0002272c1c0020000129
    """)),
    music.PlaybackMode.LOOPING_IN_BACKGROUND)

def on_update_interval():
    global bogey
    bogey = sprites.create(assets.image("""
        enemy
    """), SpriteKind.enemy)
    bogey.set_velocity(-100, 0)
    bogey.set_position(160, randint(5, 115))
    bogey.set_flag(SpriteFlag.AUTO_DESTROY, True)
    animation.run_image_animation(bogey, assets.animation("""
        enemy2
    """), 300, True)
game.on_update_interval(500, on_update_interval)
