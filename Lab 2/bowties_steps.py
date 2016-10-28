import turtle


def draw_bowtie(length):
    turtle.down()
    turtle.left(30)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(2*length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.right(30)
    turtle.up()

def draw_bowtie_one(length):
    draw_bowtie(length)
    
def draw_bowtie_two(length):
    #draw middle, big bowtie
    draw_bowtie_one(length)
    #draw smaller upper right bowtie
    turtle.left(30)
    turtle.forward(2*length)
    draw_bowtie(length/3)
    #return to middle, big bowtie center
    turtle.backward(2*length)
    turtle.right(30)
    #draw smaller upper left bowtie
    turtle.left(150)
    turtle.forward(2*length)
    draw_bowtie(length/3)
    #return to middle, big bowtie center
    turtle.backward(2*length)
    turtle.right(150)

def draw_bowtie_three(length):
    #draw middle, big bowtie
    draw_bowtie_one(length)
    #draw right side 3-bowties and return
    turtle.left(30)
    turtle.forward(2*length)
    draw_bowtie_two(length/3)
    turtle.backward(2*length)

    turtle.left(120)
    turtle.forward(2*length)
    turtle.left(180)
    draw_bowtie_two(length/3)
    turtle.left(180)
    turtle.backward(2*length)
    turtle.right(150)
    
turtle.speed(5)
draw_bowtie_three(100)
turtle.done()