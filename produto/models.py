import uuid
from django.db import models
from pessoa.models import Base
from stdimage.models import StdImageField



def get_file_path(_instance, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename

class Produto(Base):
    nome = models.CharField('Produto', max_length=150)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    codigo = models.CharField('Codigo', max_length=150)
    categoria =  models.CharField('Produto', max_length=150)
    descricao =  models.CharField('Produto', max_length=150)
    imagem = StdImageField('Imagem', upload_to=get_file_path, variations={'thumb': {'width': 480, 'height': 480, 'crop': True}})
    
    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.nome
    

