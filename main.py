def confirmar_analisis():
    print("El análisis sobrescribirá modelo/modelo.json y reemplazará sus datos actuales.")

    primera_confirmacion = input("¿Deseas continuar? (s/n): ").strip().lower()
    if primera_confirmacion != "s":
        print("Análisis cancelado.")
        return False

    segunda_confirmacion = input(
        'Para confirmar, escribe "SOBRESCRIBIR": '
    ).strip()
    if segunda_confirmacion != "SOBRESCRIBIR":
        print("Análisis cancelado.")
        return False

    return True


def main():
    while True:
        print("\n¿Qué deseas hacer?")
        print("1. Analizar los audios y generar el modelo")
        print("2. Comparar una voz usando el micrófono")
        print("3. Graficar las distribuciones del modelo")
        print("0. Salir")

        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            if confirmar_analisis():
                from analisis import main as ejecutar_analisis

                ejecutar_analisis()
        elif opcion == "2":
            from compara import main as ejecutar_comparacion

            ejecutar_comparacion()
        elif opcion == "3":
            from grafica_modelo import main as ejecutar_grafica

            ejecutar_grafica()
        elif opcion == "0":
            print("Hasta luego.")
            return
        else:
            print("Opción no válida. Intenta nuevamente.")


if __name__ == "__main__":
    main()
