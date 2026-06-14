# Turtle Graphics with Python

Bu proje size Python'un `turtle` library'sini kullandırarak çok kısa zamanda görsel şölen halini alan yuvarlaklar yaratır.

## Installation & Usage

Projeyi çalıştırmak için tek yapmanız gereken şey `terminal` üzerinden aşağıdaki komutu girmek veya kullandığınız editördeki `run` tuşuna tıklamaktır:

```bash
python main.py

İşte bu görsel şöleni arka planda yaratan o sihirli ve sade script:

import turtle as t
t.speed(0)
t.bgcolor("black")
t.color("aqua")
t.hideturtle()
for i in range(170):
    t.circle(i-5)
    t.left(5)
t.done()