def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

def main():
    monto1 = 1000
    descuento1 = calcular_descuento(monto1)
    monto_final1 = monto1 - descuento1
    print(f"Compra de ${monto1} con descuento del 10%: Descuento = ${descuento1}, Monto final = ${monto_final1}")

    monto2 = 2000
    descuento2 = calcular_descuento(monto2, 15)
    monto_final2 = monto2 - descuento2
    print(f"Compra de ${monto2} con descuento del 15%: Descuento = ${descuento2}, Monto final = ${monto_final2}")

if __name__ == "__main__":
    main()
