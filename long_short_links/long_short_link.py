import hashlib

class MarsURLEncoder:

    def __init__(self):
        self.store = {}

    def encode(self, long_url):
        """Кодирует длинную ссылку в короткую вида https://ma.rs/X7NYIol."""
        m = hashlib.sha256()
        m.update(long_url.encode())
        hash = m.hexdigest()
        self.store[hash] = long_url
        # print(f'https://ma.rs/{hash}')
        return f'https://ma.rs/{hash}'

    def decode(self, short_url):
        """Декодирует короткую ссылку вида https://ma.rs/X7NYIol в исходную."""
        key = short_url[14:]
        return self.store[key]
    

l1 = 'https://tsup.ru/mars/marsohod-1/01-09-2023/daily_job.html'
l2 = 'https://tsup.ru/impunity/01092023/whats_new/'
l3 = 'https://mars-program.ru/all/010923/plan_B.htm'

dec = MarsURLEncoder()

dec.encode(l1)
dec.encode(l2)
dec.encode(l3)

print(dec.store)
