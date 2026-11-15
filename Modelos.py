from modelos import Avio, Camisa, Pantalon, Tela
def ejecutar_pruebas():
# 1. Instanciación de telas (Composición 1 a 1)
lino_italiano = Tela(tipo="Lino Lavado", gramaje_gsm=165, costo_metro=14.0)
denim_selvedge = Tela(tipo="Mezclilla Selvedge 100% Algodón", gramaje_gsm=380,
costo_metro=18.5)
# 2. Instanciación de una Camisa (Subclase 1)
camisa_casual = Camisa(
nombre="Camisa Resort Verano",
talla="M",
tela=lino_italiano,
metros_tela=1.60,
tipo_cuello="Cubano",
manga_larga=False,
)
camisa_casual.agregar_avio(Avio("Botón de coco natural", 0.45, 7))
camisa_casual.agregar_avio(Avio("Etiqueta tejida de marca", 0.30, 1))
# 3. Instanciación de un Pantalón (Subclase 2)
jeans_clasicos = Pantalon(
nombre="Jeans Indigo Raw",
talla="32",
tela=denim_selvedge,
metros_tela=1.45,
corte="Recto (Straight Fit)",
num_bolsillos=5,
)
jeans_clasicos.agregar_avio(Avio("Cierre metálico YKK", 1.80, 1))
jeans_clasicos.agregar_avio(Avio("Botón metálico remachado", 0.90, 1))
jeans_clasicos.agregar_avio(Avio("Remache de cobre", 0.25, 6))
# 4. Ejecución de pruebas y polimorfismo
coleccion_temporada = [camisa_casual, jeans_clasicos]
for prenda in coleccion_temporada:
print("=" * 60)
print(prenda.obtener_ficha_diseno())
print("=" * 60)
if __name__ == "__main__":
ejecutar_pruebas()
