# モジュールをimport
import pygame as pg
import sys

# main関数
def main():

    # ゲームの初期化
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()

    # 背景画像を読込む
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")

    # こうかとん画像を読込む
    kk_img = pg.image.load("ex01/fig/3.png")
    kk_img = pg.transform.flip(kk_img, True, False)
    kk_imgs = [kk_img, pg.transform.rotozoom(kk_img, 10, 1.0)]

    tmr = 0

    # x1:1つ目の画像, x2:2つ目(反転)画像
    x1 = 0
    x2 = 1600

    # ゲームのループ
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        tmr += 1
        x1 -= 1
        x2 -= 1

        if x1 <= -1600:
            x1 = 1600
        
        if x2 <= -1600:
            x2 = 1600

        screen.blit(bg_img, [x1, 0])
        bg_img = pg.transform.flip(bg_img, True, False)
        screen.blit(bg_img, [x2, 0])
        bg_img = pg.transform.flip(bg_img, True, False)

        # print("tmr:" + str(tmr) + ", x1:" + str(x1) + ", x2:" + str(x2))

        # こうかとん画像を表示
        screen.blit(kk_imgs[int((tmr*0.01) % 2)], [300, 200])

        pg.display.update()
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()
