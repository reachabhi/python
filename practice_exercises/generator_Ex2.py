

def make_song(max=99, beverage='soda'):
    count = max
    while count >= 0:
        if count == 0:
            yield 'No more {}!'.format(beverage)
        if count == 1:
            yield 'Only {} bottle of {} left!'.format(count, beverage)
        if count > 1:
            yield '{} bottles of {} on the wall.'.format(count, beverage)
        count-=1

kombucha_song = make_song(5, "kombucha")

print(next(kombucha_song)) # '5 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '4 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '3 bottles of kombucha on the wall.'
print(next(kombucha_song)) # '2 bottles of kombucha on the wall.'
print(next(kombucha_song)) # 'Only 1 bottle of kombucha left!'
print(next(kombucha_song)) # 'No more kombucha!'
print(next(kombucha_song)) # StopIteration
default_song = make_song()
print(next(default_song)) # '99 bottles of soda on the wall.'