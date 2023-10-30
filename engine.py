import pygame


class terminal:
    def __init__(self, wd, height, width):
        self.wd = wd
        self.font = pygame.font.SysFont('Agency FB', 14)
        self.commands = {'pwd': pwd}
        self.info = {'command text': '', 'command history': []}
        self.WIN = pygame.display.set_mode((height, width))
        self.max_len = 760
        self.max_his = 60
        self.height = height
        self.width = width

    def draw(self):
        self.WIN.fill((0, 0, 0))

        text = '>>> ' + self.info['command text']
        text_surface = self.font.render(text, True, (255, 255, 255))
        tw = text_surface.get_width()
        th = text_surface.get_height()
        sw = 300
        sh = th * (len(self.info['command history'])+1) + 10
        surf = pygame.Surface((sw, sh))
        for i in range(len(self.info['command history'])):
            txt = self.info['command history'][i]
            txt_surface = self.font.render(txt, True, (200, 200, 200))
            surf.blit(txt_surface, (5, 5+i*th))
        surf.blit(text_surface, (5, sh-th-5))
        # surf.set_alpha(100)
        self.WIN.blit(surf, (10, self.height-sh))
        pygame.display.update()

    def list2str(self, mylist):
        string = ''
        for word in mylist:
            string += word
            string += ' '
        return string
    
    def get_pressed(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                # print('key pressed')
                if event.key == pygame.K_BACKSPACE:
                    self.info['command text'] = self.info['command text'][:-1]
                elif event.key == pygame.K_RETURN:
                    if len(self.info['command text']) > 0:
                        self.info['command history'].append(self.info['command text'])
                        if len(self.info['command history']) > self.max_his:
                            self.info['command history'] = self.info['command history'][-30:]
                        self.unpack_str(self.info['command text'])
                    self.info['command text'] = ''
                elif event.key == pygame.K_TAB:
                    if len(self.info['command text']) > 0:
                        self.complete_str()
                elif event.unicode.isprintable() and len(self.info['command text']) < self.max_len:
                    self.info['command text'] += event.unicode

    def unpack_str(self, mystring):
        cmd_list = mystring.split(' ')
        for cmd in cmd_list:
            if cmd in self.commands:
                if callable(self.commands[cmd]):
                    fn = self.commands[cmd]
                    fn(self)
                # elif type(self.commands[cmd]) is dict:
                #     d = d[cmd]

    def complete_str(self):
        cmd_list = self.info['command text'].split(' ')
        d = self.commands
        for cmd in cmd_list:
            if cmd in d:
                if type(d[cmd]) is dict:
                    d = d[cmd]
            else:
                lets = len(cmd)
                comp_list = []
                for key in d.keys():
                    if len(key) >= lets and key[:lets] == cmd:
                        comp_list.append(key)
                if len(comp_list) == 1:
                    # print(cmd_list)
                    new_list = cmd_list[:cmd_list.index(cmd)]
                    new_list.append(comp_list[0])
                    # print(new_list)
                    new_string = self.list2str(new_list)
                    self.info['command text'] = new_string
                elif len(comp_list) > 1:
                    self.info['command history'].append('_____________________________')
                    for comp in comp_list:
                        self.info['command history'].append(comp)
                    self.info['command history'].append('_____________________________')


def pwd(t):
    t.info['command history'].append(t.wd)
