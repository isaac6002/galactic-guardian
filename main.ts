controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    while (controller.A.isPressed()) {
        projectile = sprites.createProjectileFromSprite(assets.image`shot`, Spaceplane, 200, 0)
        music.play(music.createSoundEffect(
        WaveShape.Square,
        5000,
        1,
        246,
        0,
        400,
        SoundExpressionEffect.Tremolo,
        InterpolationCurve.Curve
        ), music.PlaybackMode.InBackground)
        pause(350)
    }
})
info.onLifeZero(function () {
    game.gameOver(false)
})
info.onScore(70, function () {
    game.gameOver(true)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Enemy, function (sprite, otherSprite) {
    sprites.destroy(otherSprite, effects.warmRadial, 60)
    scene.cameraShake(2, 500)
    info.changeScoreBy(1)
    sprites.destroy(sprite, effects.fire, 9)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    info.changeLifeBy(-1)
    scene.cameraShake(4, 500)
})
let enemy1: Sprite = null
let projectile: Sprite = null
let Spaceplane: Sprite = null
scene.setBackgroundImage(assets.image`background`)
scroller.scrollBackgroundWithSpeed(-10, 0)
Spaceplane = sprites.create(assets.image`myImage0`, SpriteKind.Player)
controller.moveSprite(Spaceplane, 100, 100)
Spaceplane.setStayInScreen(true)
info.setLife(3)
info.setScore(0)
game.splash("iniciar")
music.play(music.createSong(hex`0078000408040300001c00010a006400f401640000040000000000000000000000000005000004180000002000012920004000012540006000012760008000012203001c0001dc00690000045e0100040000000000000000000005640001040003180000002000012020004000011d40006000011e60008000011b07001c00020a006400f4016400000400000000000000000000000000000000032a0000000400012710001400011e20002400012440004400012750005400012460006400011e700074000125`), music.PlaybackMode.LoopingInBackground)
game.onUpdate(function () {
    enemy1.x += controller.dx(63)
    enemy1.y += controller.dy(1)
})
game.onUpdateInterval(500, function () {
    enemy1 = sprites.create(img`
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . f f f f f . . . . . 
        . . . . . f c c c c 8 f . . . . 
        . . . f f f c c c c 8 f . . . . 
        . . f c 1 1 b c c c 8 9 f . . . 
        . f c c f f b c c e 8 8 9 f f . 
        . f c c c 4 c c c c 8 8 9 9 9 f 
        . f c c c 4 c c c c 8 8 9 9 9 f 
        . f c c f f b c c e 8 8 9 f f . 
        . . f c 1 1 b c c c 8 9 f . . . 
        . . . f f f c c c c 8 f . . . . 
        . . . . . f c c c c 8 f . . . . 
        . . . . . . f f f f f . . . . . 
        . . . . . . . . . . . . . . . . 
        . . . . . . . . . . . . . . . . 
        `, SpriteKind.Enemy)
    enemy1.setVelocity(-74, 0)
    enemy1.setPosition(160, randint(5, 105))
    enemy1.setFlag(SpriteFlag.AutoDestroy, true)
    animation.runImageAnimation(
    enemy1,
    assets.animation`enemy2`,
    200,
    true
    )
})
