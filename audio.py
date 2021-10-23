import pygame as pg
import time

pg.mixer.init()  

class sintetizador:
    def __init__(self):
        self.vocales = ['A','E','I','O','U']
        self.letras_sinvocales = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        self.letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        self.combinaciones = ['BA', 'CA', 'DA', 'FA', 'GA', 'HA', 'JA', 'KA', 'LA', 'MA', 'NA', 'PA', 'QA', 'RA', 'SA', 'TA', 'VA', 'WA', 'XA', 'YA', 'ZA', 'BE', 'CE', 'DE', 'FE', 'GE', 'HE', 'JE', 'KE', 'LE', 'ME', 'NE', 'PE', 'QE', 'RE', 'SE', 'TE', 'VE', 'WE', 'XE', 'YE', 'ZE', 'BI', 'CI', 'DI', 'FI', 'GI', 'HI', 'JI', 'KI', 'LI', 'MI', 'NI', 'PI', 'QI', 'RI', 'SI', 'TI', 'VI', 'WI', 'XI', 'YI', 'ZI', 'BO', 'CO', 'DO', 'FO', 'GO', 'HO', 'JO', 'KO', 'LO', 'MO', 'NO', 'PO', 'RO', 'SO', 'TO', 'VO', 'WO', 'XO', 'YO', 'ZO', 'BU', 'CU', 'DU', 'FU', 'GU', 'HU', 'JU', 'KU', 'LU', 'MU', 'NU', 'PU', 'RU', 'SU', 'TU', 'VU', 'WU', 'XU', 'YU', 'ZU']
        self.combinaciones3 = ['RRA', 'RRE', 'RRI', 'RRO', 'RRU', 'CHA', 'CHE', 'CHI', 'CHO', 'CHU', 'GUE', 'GUI']
    
    def recortar(self,texto):
        conteo = 0
        texto = texto.upper()
        for t in texto:
            conteo += 1

        elementos = {}

        #Espacios
        espacios = {}
        for veces in range(texto.count(" ")):
            busq = texto.find(str(" "))
            texto = texto.replace(" ", "_", 1)
            espacios[busq] = "SPACE"

        elementos["5"] = espacios

        #0 serían las letras que suenan
        cero = {}
        for e in self.letras_sinvocales:
            for veces in range(texto.count(e)):
                busq = texto.find(str(e))
                if (texto[busq:busq+2] not in self.combinaciones and texto[busq:busq+3] not in self.combinaciones3):

                    if(texto[busq-1] in self.vocales):
                        texto = texto.replace(e, " ", 1)
                        print(e)
                        cero[busq] = "-"+str(e)
        elementos[0] = cero

        tres = {}
        for e in self.combinaciones3:
            for veces in range(texto.count(e)):
                busq = texto.find(str(e))
                texto = texto.replace(e, "   ", 1)
                tres[busq] = e
        elementos[3] = tres

        dos = {}
        for e in self.combinaciones:
            for veces in range(texto.count(e)):
                busq = texto.find(str(e))
                texto = texto.replace(e, "  ", 1)
                dos[busq] = e
        elementos[2] = dos


        uno = {}
        for e in self.letras:
            for veces in range(texto.count(e)):
                busq = texto.find(str(e))
                texto = texto.replace(e, " ", 1)
                uno[busq] = e
        elementos[1] = uno


        todos_valores = {}

        for elemento in elementos:
            llaves = elementos[elemento].keys()
            valores = elementos[elemento].values()
            for llave in llaves:
                todos_valores[llave] = str(elementos[elemento][llave])

                    # archivo = f"audio/{parte}.wav"
                    # pg.mixer.Sound(archivo).play()
                    # time.sleep(0.3)


        todos_valores_list = sorted(todos_valores)
        for h in todos_valores_list:
            print(todos_valores[h])
            archivo = f"audio/{todos_valores[h]}.wav"            
            a = pg.mixer.Sound(archivo)
            longitud = a.get_length()
            a.play()
            time.sleep(longitud/2)
                
        #mitad_cont = round(conteo/3)
        # for x in self.combinaciones3:
        #     busq = texto.find(x)
        #     if(busq >= 0):
        #         archivo = f"audio/{x}.wav"
        #         pg.mixer.Sound(archivo).play()
        #         time.sleep(0.3)
        #         #texto[busq:busq+3] = ""
        #         print(texto)

        # par_tres = texto[conjunto:conjunto+3].upper()
        # if par_tres in self.combinaciones3:
        #     archivo = f"audio/{par_tres}.wav"
        #     pg.mixer.Sound(archivo).play()
        #     time.sleep(0.3)
        #     print(par_tres)
        # else:
        #     par_uno = par_tres[0:1]
        #     par_dos = par_tres[1:2]

        #     if par_uno in self.combinaciones:
        #         archivo = f"audio/{par_uno}.wav"
        #         pg.mixer.Sound(archivo).play()
        #         time.sleep(0.3)
        #     elif par_dos in self.combinaciones:
        #         archivo = f"audio/{par_dos}.wav"
        #         pg.mixer.Sound(archivo).play()
        #         time.sleep(0.3)

        # pg.mixer.Sound('audio/E.wav').play()
        # time.sleep(0.2)
        

def main():
    screen = pg.display.set_mode((640, 480))
    font = pg.font.Font(None, 32)
    clock = pg.time.Clock()
    input_box = pg.Rect(100, 100, 140, 32)
    color_inactive = pg.Color('lightskyblue3')
    color_active = pg.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = ""
    done = False
    st = sintetizador()

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.MOUSEBUTTONDOWN:
                # If the user clicked on the input_box rect.
                if input_box.collidepoint(event.pos):
                    # Toggle the active variable.
                    active = not active
                else:
                    active = False
                # Change the current color of the input box.
                color = color_active if active else color_inactive
            if event.type == pg.KEYDOWN:
                if active:
                    if event.key == pg.K_RETURN:
                        print("El texto es:",text) ###Información importante papá
                        st.recortar(text)
                        text = ""
                    elif event.key == pg.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width()+10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x+5, input_box.y+5))
        # Blit the input_box rect.
        pg.draw.rect(screen, color, input_box, 2)

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()