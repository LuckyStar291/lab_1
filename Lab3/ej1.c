#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/debug.h"
#include "driverlib/gpio.h"
#include "driverlib/sysctl.h"

// Definir el número máximo y mínimo del contador
#define MAX_COUNTER 15
#define MIN_COUNTER 0

// Variable para almacenar el valor del contador
uint32_t counter = 0;

#ifdef DEBUG
void __error__(char *pcFilename, uint32_t ui32Line)
{
    while(1);
}
#endif
void LedChange(int counter){
    GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_1, (counter & 0x1) ? GPIO_PIN_1 : 0);  // LED 1 (LSB)
    GPIOPinWrite(GPIO_PORTN_BASE, GPIO_PIN_0, (counter & 0x2) ? GPIO_PIN_0 : 0);  // LED 2
    GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_4, (counter & 0x4) ? GPIO_PIN_4 : 0);  // LED 3
    GPIOPinWrite(GPIO_PORTF_BASE, GPIO_PIN_0, (counter & 0x8) ? GPIO_PIN_0 : 0);  // LED 4 (MSB)
}

int main(void)
{
    volatile uint32_t ui32Loop;

    // Habilitar los puertos GPIO para los LEDs y los interruptores
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPION);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOF);
    SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOJ); // Para los interruptores en PJ0-PJ1

    // Asegurarse de que los puertos GPIO están listos
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPION)) {}
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOF)) {}
    while(!SysCtlPeripheralReady(SYSCTL_PERIPH_GPIOJ)) {}

    // Configurar los pines de los LEDs como salida
    GPIOPinTypeGPIOOutput(GPIO_PORTN_BASE, GPIO_PIN_0 | GPIO_PIN_1);
    GPIOPinTypeGPIOOutput(GPIO_PORTF_BASE, GPIO_PIN_0 | GPIO_PIN_4);

    // Configurar los pines de los interruptores como entrada
    GPIOPinTypeGPIOInput(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1);

    // Habilitar las resistencias de Pull-Up para los interruptores
    GPIOPadConfigSet(GPIO_PORTJ_BASE, GPIO_PIN_0 | GPIO_PIN_1, GPIO_STRENGTH_2MA, GPIO_PIN_TYPE_STD_WPU);

    while(1)
    {
        // Comprobar si el interruptor 1 (PJ0) está presionado (aumentar el contador)
        if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_0) == 0) // 0 indica que el interruptor está presionado
        {
            while (counter < MAX_COUNTER){
                counter++;
                for(ui32Loop = 0; ui32Loop < 200000; ui32Loop++)
                {
                }
                LedChange(counter);
                SysCtlDelay(120000000/10);
            }
        }

        if (GPIOPinRead(GPIO_PORTJ_BASE, GPIO_PIN_1) == 0) // 0 indica que el interruptor está presionado
        {
            while (counter > MIN_COUNTER) {
                counter--; // Decrementar el contador
                for(ui32Loop = 0; ui32Loop < 200000; ui32Loop++)
                {
                }
                LedChange(counter);
                SysCtlDelay(120000000/10);
            }
        }

        for(ui32Loop = 0; ui32Loop < 200000; ui32Loop++)
        {
        }
    }
}
