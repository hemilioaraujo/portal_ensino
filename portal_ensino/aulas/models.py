from django.db import models


class Aulas(models.Model):
    titulo = models.TextField(blank=False, null=False)
    link = models.TextField(blank=False, null=False)

    class Meta:
        verbose_name_plural = "Aulas"

    def __str__(self):
        return f'{self.id} - {self.titulo}'


    def popular_tabela_aulas(self):
        Aulas.objects.create(
            id=1,
            titulo='Sistema de Equações',
            link='https://www.youtube.com/watch?v=pbFZW1eTnkk&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=1')
        Aulas.objects.create(
            id=2,
            titulo='Introdução ao Escalonamento',
            link='https://www.youtube.com/watch?v=wvrMO_C-cdE&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=2')
        Aulas.objects.create(
            id=3,
            titulo='Pivô e Escalonamento',
            link='https://www.youtube.com/watch?v=a_IfBj7Gdfs&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=3')
        Aulas.objects.create(
            id=4,
            titulo='Discussão de Sistema',
            link='https://www.youtube.com/watch?v=ganCbJlJTbE&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=4')
        Aulas.objects.create(
            id=5,
            titulo='Resolução de Sistema com Escalonamento',
            link='https://www.youtube.com/watch?v=eTEPbbhL2hM&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=5')
        Aulas.objects.create(
            id=6,
            titulo='Discussão de Sistema - Gauss',
            link='https://www.youtube.com/watch?v=IQj37-tv5e4&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=6')
        Aulas.objects.create(
            id=7,
            titulo='Resolução de Sistema por Gauss',
            link='https://www.youtube.com/watch?v=YXPuZFWGmyw&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=7')
        Aulas.objects.create(
            id=8,
            titulo='Vetores',
            link='https://www.youtube.com/watch?v=0Gp1QgdhujE&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=8')
        Aulas.objects.create(
            id=9,
            titulo='Operações com vetores',
            link='https://www.youtube.com/watch?v=z1DQ3vXvGLw&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=9')
        Aulas.objects.create(
            id=10,
            titulo='Combinação Linear de Vetores',
            link='https://www.youtube.com/watch?v=eB7KJKV2k-E&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=10')
        Aulas.objects.create(
            id=11,
            titulo='Combinação Linear - Ex1',
            link='https://www.youtube.com/watch?v=8peVbC0j6aI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=11')
        Aulas.objects.create(
            id=12,
            titulo='Combinação Linear - Ex2',
            link='https://www.youtube.com/watch?v=MYH54JuIj0Y&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=12')
        Aulas.objects.create(
            id=13,
            titulo='Combinação Linear - Ex3',
            link='https://www.youtube.com/watch?v=7MVG47_THHg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=13')
        Aulas.objects.create(
            id=14,
            titulo='Combinação Linear - Ex4',
            link='https://www.youtube.com/watch?v=K6yWkn59-JI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=14')
        Aulas.objects.create(
            id=15,
            titulo='Dependência Linear',
            link='https://www.youtube.com/watch?v=1NQgheFnX9A&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=15')
        Aulas.objects.create(
            id=16,
            titulo='Dependência Linear - Ex 1',
            link='https://www.youtube.com/watch?v=jA-6Xcw8__E&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=16')
        Aulas.objects.create(
            id=17,
            titulo='Dependência Linear - Ex 2',
            link='https://www.youtube.com/watch?v=wgIGAY5nQk0&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=17')
        Aulas.objects.create(
            id=18,
            titulo='Dependência Linear - Ex 3',
            link='https://www.youtube.com/watch?v=V7ysHtEi1q4&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=18')
        Aulas.objects.create(
            id=19,
            titulo='Dependência Linear - Ex 4',
            link='https://www.youtube.com/watch?v=LigrD3eurZs&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=19')
        Aulas.objects.create(
            id=20,
            titulo='Espaço Vetorial - Ex1',
            link='https://www.youtube.com/watch?v=e8kAs458cVI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=20')
        Aulas.objects.create(
            id=21,
            titulo='Espaço Vetorial - Ex2',
            link='https://www.youtube.com/watch?v=KXVCjPjgpq4&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=21')
        Aulas.objects.create(
            id=22,
            titulo='Subespaço Vetorial - Ex1',
            link='https://www.youtube.com/watch?v=XxUWCQaVwKM&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=22')
        Aulas.objects.create(
            id=23,
            titulo='Subespaço Vetorial - Ex2',
            link='https://www.youtube.com/watch?v=HnGwjpfp3Gc&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=23')
        Aulas.objects.create(
            id=24,
            titulo='Subespaço Vetorial - Ex3',
            link='https://www.youtube.com/watch?v=j9XnjqEUUkQ&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=24')
        Aulas.objects.create(
            id=25,
            titulo='Subespaço Vetorial - Ex4',
            link='https://www.youtube.com/watch?v=AtMFysEdlag&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=25')
        Aulas.objects.create(
            id=26,
            titulo='Subespaço Vetorial - Ex5',
            link='https://www.youtube.com/watch?v=YAxsFPVv3ds&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=26')
        Aulas.objects.create(
            id=27,
            titulo='Subespaço Gerado - Ex.1',
            link='https://www.youtube.com/watch?v=lqfAoCG1CMY&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=27')
        Aulas.objects.create(
            id=28,
            titulo='Subespaço Gerado - Ex.2',
            link='https://www.youtube.com/watch?v=zE9g8XT2oMg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=28')
        Aulas.objects.create(
            id=29,
            titulo='Subespaço Gerado - Ex.3',
            link='https://www.youtube.com/watch?v=WQiEA4_PbbU&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=29')
        Aulas.objects.create(
            id=30,
            titulo='Base de um Espaço Vetorial',
            link='https://www.youtube.com/watch?v=1s1d_z5iQbk&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=30')
        Aulas.objects.create(
            id=31,
            titulo='Como calcular uma base geradora',
            link='https://www.youtube.com/watch?v=H_yOpYU7hTY&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=31')
        Aulas.objects.create(
            id=32,
            titulo='Extraindo a base geradora de um subespaço. Exercício 1',
            link='https://www.youtube.com/watch?v=5dst5A_ch0k&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=32')
        Aulas.objects.create(
            id=33,
            titulo='Extraindo a base geradora de um subespaço. Exercício 2',
            link='https://www.youtube.com/watch?v=5kAQ_r1yWXg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=33')
        Aulas.objects.create(
            id=34,
            titulo='Extraindo a base geradora de um subespaço. Exercício 3',
            link='https://www.youtube.com/watch?v=ELo65Qjv5Dg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=34')
        Aulas.objects.create(
            id=35,
            titulo='Extraindo a base geradora de um subespaço. Exercício 4',
            link='https://www.youtube.com/watch?v=FUOxfqt8zrM&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=35')
        Aulas.objects.create(
            id=36,
            titulo='Como extrair uma base geradora de um conjunto de vetores',
            link='https://www.youtube.com/watch?v=shH9uTczXDI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=36')
        Aulas.objects.create(
            id=37,
            titulo='Subespaço gerado a partir de um conjunto de vetores',
            link='https://www.youtube.com/watch?v=ZRuJXCG2CpI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=37')
        Aulas.objects.create(
            id=38,
            titulo='Mudança de base geradora',
            link='https://www.youtube.com/watch?v=muA2fcZGQXs&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=38')
        Aulas.objects.create(
            id=39,
            titulo='Mudança de base sem uso de matriz inversa',
            link='https://www.youtube.com/watch?v=U55o4HTmPF0&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=39')
        Aulas.objects.create(
            id=40,
            titulo='Mudança de base . Vetor com 3 componentes',
            link='https://www.youtube.com/watch?v=Qta17OWjsFs&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=40')
        Aulas.objects.create(
            id=41,
            titulo='Dedução da Fórmula Matriz Mudança de base',
            link='https://www.youtube.com/watch?v=4bc1We6Akkc&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=41')
        Aulas.objects.create(
            id=42,
            titulo='Mudança de Base de um Vetor com a Matriz Mudança de base',
            link='https://www.youtube.com/watch?v=3F3E8DcivKg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=42')
        Aulas.objects.create(
            id=43,
            titulo='Mudança de base demonstrado graficamente',
            link='https://www.youtube.com/watch?v=9UozHl91Zdg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=43')
        Aulas.objects.create(
            id=44,
            titulo='Introdução a Transformação Linear',
            link='https://www.youtube.com/watch?v=O3rou_UUIIg&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=44')
        Aulas.objects.create(
            id=45,
            titulo='Transformação Linear',
            link='https://www.youtube.com/watch?v=h96mnXdcsaI&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=45')
        Aulas.objects.create(
            id=46,
            titulo='Transformação Linear',
            link='https://www.youtube.com/watch?v=ZB28kpo0VTQ&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=46')
        Aulas.objects.create(
            id=47,
            titulo='Propriedades da Transformação Linear',
            link='https://www.youtube.com/watch?v=xYAbFnh4Rco&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=47')
        Aulas.objects.create(
            id=48,
            titulo='Propriedades da Transformação Linear',
            link='https://www.youtube.com/watch?v=6EM6dBEGc-g&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=48')
        Aulas.objects.create(
            id=49,
            titulo='Dada imagem, ache a Transformação Linear',
            link='https://www.youtube.com/watch?v=aera-zZlBMs&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=49')
        Aulas.objects.create(
            id=50,
            titulo='Como obter a lei de uma Transformação Linear',
            link='https://www.youtube.com/watch?v=igvfXiYiwAY&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=50')
        Aulas.objects.create(
            id=51,
            titulo='Como obter a lei de uma Transformação Linear',
            link='https://www.youtube.com/watch?v=inBnKDHEJ2s&list=PLE6qFDd4x9w_Q3Dsh6j2i6Q1IxSyvyTnC&index=51')
