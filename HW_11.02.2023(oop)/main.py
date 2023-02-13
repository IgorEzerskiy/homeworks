class Element:
    scales = {'K': lambda x: x - 273.15,
              'F': lambda x: (x - 32) / 1.8,
              'C': lambda x: x}
    scales_for_agg = {'K': lambda x: x + 273.15,
                      'F': lambda x: (x * 1.8) + 32,
                      'C': lambda x: x}

    def __init__(self, melting_t, boiling_t):
        self.melting_t = melting_t
        self.boiling_t = boiling_t

    def agg_state(self, temp, scale='C'):
        self.boiling_t = self.scales_for_agg.get(scale)(self.boiling_t)
        self.melting_t = self.scales_for_agg.get(scale)(self.melting_t)
        print(self.boiling_t, ' ', self.melting_t)
        if temp > self.boiling_t:
            return f'Element are boiling with temperature - {temp}{scale}'
        elif self.melting_t <= temp <= self.boiling_t:
            return f'Element are melting with temperature - {temp}{scale}'
        else:
            return f'The element retained its state of aggregation at a temperature of - {temp}{scale}'

    def convert_to_c(self, temp, scale='C'):
        return f'{temp}{scale}, {round(self.scales.get(scale)(temp), 2)}°C'


if __name__ == '__main__':
    elem = Element(melting_t=560, boiling_t=1500)
    print(elem.agg_state(temp=1500, scale='K'))
    print(elem.convert_to_c(temp=56, scale='K'))
