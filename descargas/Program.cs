using System;

namespace ConsoleApp1
{
    class Program
    {
        struct dino //estructura del programa
        {
            public int especie;
            public string name;
            public double peso;
            public double largo;
            public string[] dieta;
            public double costo;
            public string esp;
        }
        static void Llenado(dino[] dinos) //esta funcion se encarga de llenar la éstructura 
        {
            int cont = 0;

            char resp1;
            for (cont = 0; cont < dinos.Length; cont++)
            {
                dinos[cont].dieta = new string[4];
                do
                {
                    Console.WriteLine("Su dinosaurio numero " + (cont + 1) + " ¿Es herbívoro o carnívoro? ");
                    Console.WriteLine("Marque H para herbívoros y C para carnívoros");
                    resp1 = char.Parse(Console.ReadLine());
                    if (resp1 != 'C' && resp1 != 'H' && resp1 != 'c' && resp1 != 'h')
                        Console.WriteLine("Porfavor seleccione el caracter correcto");
                } while (resp1 != 'C' && resp1 != 'H' && resp1 != 'c' && resp1 != 'h');//validación de tipo de dieta 
                if (resp1 == 'C' || resp1 == 'c')
                {
                    do // hay una validación para elegir el tipo de dinosaurio que se quiere 
                    {
                        Console.WriteLine("Las opciones para doinosaurios carnivoros son:");
                        Console.WriteLine("1-Tyrannosaurus rex $39,000,000");
                        Console.WriteLine("2-Velociraptor $7,000,000");
                        Console.WriteLine("3-Allosaurus $23,000,000");
                        Console.WriteLine("4-Carnotaurus $18,000,000");
                        Console.WriteLine("5-Spinosaurus $29,900,000");
                        dinos[cont].especie = int.Parse(Console.ReadLine());
                        if (dinos[cont].especie != 1 && dinos[cont].especie != 2 && dinos[cont].especie != 3 && dinos[cont].especie != 4 && dinos[cont].especie != 5)
                            Console.WriteLine("Porfavor seleccione una opción del 1 al 5");
                    } while (dinos[cont].especie != 1 && dinos[cont].especie != 2 && dinos[cont].especie != 3 && dinos[cont].especie != 4 && dinos[cont].especie != 5);
                }
                else if (resp1 == 'H' || resp1 == 'h')
                {
                    do
                    {
                        Console.WriteLine("Las opciones de herbivoros son:");
                        Console.WriteLine("6-Ankylosaurus $27,000,000");
                        Console.WriteLine("7-Brachiosaurus $169,000,000");
                        Console.WriteLine("8-Stegosaurus $12,000,000");
                        Console.WriteLine("9-Triceratops $28,900,000");
                        dinos[cont].especie = int.Parse(Console.ReadLine());
                        if (dinos[cont].especie != 6 && dinos[cont].especie != 7 && dinos[cont].especie != 8 && dinos[cont].especie != 9)
                            Console.WriteLine("Porfavor seleccione una opción del 6 al 9");
                    } while (dinos[cont].especie != 6 && dinos[cont].especie != 7 && dinos[cont].especie != 8 && dinos[cont].especie != 9);
                }
                Console.WriteLine("¿Cual será el nombre del dinosaurio " + (cont + 1) + "?");
                dinos[cont].name = Console.ReadLine();
                dinos[cont].name = dinos[cont].name.ToLower();
                switch (dinos[cont].especie)
                {
                    //Casos por dinosaurio para calculos
                    case 1:
                        {
                            Console.WriteLine("Promedio: Peso 7,000, Largo: 12");
                            calculos(dinos, 7000, 12, cont, dinos[cont].name);
                            dinos[cont].esp = "Tyrannosaurus rex";
                            break;

                        }
                    case 2:
                        {
                            Console.WriteLine("Promedio: Peso 30, Largo: 2");
                            calculos(dinos, 30, 2, cont, dinos[cont].name);
                            dinos[cont].esp = "Velociraptor";
                            break;
                        }
                    case 3:
                        {
                            Console.WriteLine("Promedio: Peso 3,500, Largo: 10");
                            calculos(dinos, 3500, 10, cont, dinos[cont].name);
                            dinos[cont].esp = "Allosaurus";
                            break;
                        }
                    case 4:
                        {
                            Console.WriteLine("Promedio: Peso 2,100, Largo: 9");
                            calculos(dinos, 2100, 9, cont, dinos[cont].name);
                            dinos[cont].esp = "Carnotaurus";
                            break;
                        }
                    case 5:
                        {
                            Console.WriteLine("Promedio: Peso 6,000, Largo: 20");
                            calculos(dinos, 6000, 20, cont, dinos[cont].name);
                            dinos[cont].esp = "Spinosaurus";
                            break;
                        }
                    case 6:
                        {
                            Console.WriteLine("Promedio: Peso 6,000, Largo: 9");
                            calculos(dinos, 6000, 9, cont, dinos[cont].name);
                            dinos[cont].esp = "Ankylosaurus";
                            break;
                        }
                    case 7:
                        {
                            Console.WriteLine("Promedio: Peso 50,000, Largo: 25");
                            calculos(dinos, 50000, 25, cont, dinos[cont].name);
                            dinos[cont].esp = "Brachiosaurus";
                            break;
                        }
                    case 8:
                        {
                            Console.WriteLine("Promedio: Peso 3,000, Largo: 9");
                            calculos(dinos, 3000, 9, cont, dinos[cont].name);
                            dinos[cont].esp = "Stegosaurus";
                            break;
                        }
                    case 9:
                        {
                            Console.WriteLine("Promedio: Peso 7,000, Largo: 7");
                            calculos(dinos, 7000, 7, cont, dinos[cont].name);
                            dinos[cont].esp = "Triceratops";
                            break;
                        }
                }
                dinos[cont].costo = Fx(dinos, cont, resp1);
            }
        }
        static double Fx(dino[] arre, int cont, char co)
        {
            int cant = 0, opción;
            double total = 0;
            if (co == 'c' || co == 'C')
            {
                Console.WriteLine("Menú para dinosaurios carnivoros");
                Console.WriteLine("1.-Pollo");
                Console.WriteLine("2.-Res");
                Console.WriteLine("3.-Cabra");
                Console.WriteLine("Seleccione el número de la opción deseada.");
                for (cant = 0; cant < 4; cant++)
                {
                    do
                    {
                        Console.WriteLine("¿Que alimento le dara la semana " + (cant + 1) + "?");// cuando se selecciona la opción carnívora se va al menú
                        opción = int.Parse(Console.ReadLine());
                        switch (opción)// en todos los casos del switch multiplica el costo del kilogramo del alimento por el 140% del peso correspondiente al dinosaurio 
                        {
                            case 1:
                                {
                                    arre[cont].dieta[cant] = "pollo";
                                    total = total + arre[cont].peso * 1.40;
                                    break;
                                }
                            case 2:
                                {
                                    arre[cont].dieta[cant] = "res";
                                    total = total + arre[cont].peso * 1.40 * 1.8;
                                    break;
                                }
                            case 3:
                                {
                                    arre[cont].dieta[cant] = "cabra";
                                    total = total + arre[cont].peso * 1.40 * 1.3;
                                    break;
                                }
                            default:
                                {
                                    Console.WriteLine("La opción seleccionada no existe");
                                    break;
                                }
                        }
                    } while (opción != 1 && opción != 2 && opción != 3);
                }
            }
            else if (co == 'h' || co == 'H')// cuando se selecciona el tipo de dieta se va a la opción herbívora que tiene un menú 
            {
                Console.WriteLine("Menú para dinosaurios herbívoros");
                Console.WriteLine("1.-Patatas");
                Console.WriteLine("2.-Hierbas");
                Console.WriteLine("3.-Trigo");
                Console.WriteLine("Seleccione el número de la opción deseada.");
                for (cant = 0; cant < 4; cant++)
                {
                    do
                    {
                        Console.WriteLine("¿Que alimento le dara la semana " + (cant + 1) + "?");
                        opción = int.Parse(Console.ReadLine());
                        switch (opción)
                        {
                            case 1:
                                {
                                    arre[cont].dieta[cant] = "patatas";
                                    total = total + arre[cont].peso * .03;
                                    break;
                                }
                            case 2:
                                {
                                    arre[cont].dieta[cant] = "hierbas";
                                    total = total + arre[cont].peso * 1.40 * .07;
                                    break;
                                }
                            case 3:
                                {
                                    arre[cont].dieta[cant] = "trigo";
                                    total = total + arre[cont].peso * 1.40 * .2;
                                    break;
                                }
                            default:
                                {
                                    Console.WriteLine("La opción seleccionada no existe");
                                    break;
                                }
                        }
                    } while (opción != 1 && opción != 2 && opción != 3);//validación 
                }
            }
            return total;
        }
        static void calculos(dino[] z, int pes, int larg, int Kant, string nom)// esta función sirve para tener los datos del peso y largo del dinosaurio para calcular su hábitat, costo de mantenimiento, alimentación etc.
        {
            do
            {
                Console.WriteLine("Escribe el peso de " + nom);
                z[Kant].peso = double.Parse(Console.ReadLine());
                if (z[Kant].peso < (pes * .6))
                    Console.WriteLine("El dinosaurio tiene un peso menor al rango");
                if (z[Kant].peso > (pes * 1.4))
                    Console.WriteLine("El dinosaurio tiene un peso mayor al rango");
            }
            while (z[Kant].peso < (pes * .6) || z[Kant].peso > (pes * 1.4));// validación peso
            do
            {
                Console.WriteLine("Escribe el largo de " + nom);
                z[Kant].largo = double.Parse(Console.ReadLine());
                if (z[Kant].largo < (larg * .7) || z[Kant].largo > (larg * 1.3))
                    Console.WriteLine("El largo se encuentra fuera de rango");

            }
            while (z[Kant].largo < (larg * .7) || z[Kant].largo > (larg * 1.3));//validación largo

        }
        static void imprimir(dino[] imp)// función del menú que se encarga de imprimir la tabla 2
        {
            int cent, cint;
            Console.WriteLine("Especie\t\tNombre\t\tCosto de Habitat\tPlan de Alimentación\tCosto Comida Mensual");
            for (cent = 0; cent < imp.Length; cent++)
            {
                Console.Write(imp[cent].esp + "\t\t" + imp[cent].name + "\t\t$" + (imp[cent].largo * 269 * 6.9) + "\t\t");
                for (cint = 0; cint < 4; cint++)
                {
                    Console.Write(imp[cent].dieta[cint] + " ");
                }
                Console.Write("\t\t$" + imp[cent].costo);
                Console.WriteLine("");
            }
        }
        static double invi(dino[] dan)//funcion del menú opción 1 que se encarga de calcular la inversión inicial del hábitat por tamaño del dinosaurio 
        {
            int cal;
            double más = 0;
            for (cal = 0; cal < dan.Length; cal++)
                switch (dan[cal].especie)
                {
                    case 1:
                        {
                            más = más + 39000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 2:
                        {
                            más = más + 7000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 3:
                        {
                            más = más + 23000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 4:
                        {
                            más = más + 18000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 5:
                        {
                            más = más + 29900000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 6:
                        {
                            más = más + 27000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 7:
                        {
                            más = más + 169000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 8:
                        {
                            más = más + 12000000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                    case 9:
                        {
                            más = más + 28900000 + dan[cal].largo * 269 * 49;
                            break;
                        }
                }
            return más;
        }
        static double mens(dino[] dsa) // función que regresa la mensualidad de mantenimiento por dinosaurio 
        {
            int cel;
            double otro = 0;
            for (cel = 0; cel < dsa.Length; cel++)
            {
                otro = otro + dsa[cel].costo + dsa[cel].largo * 269 * 6.9;
            }
            return otro * 12;
        }
        static void buscar(dino[] woke)//función que busca dinosaurio por nombre.
        {
            int core, fake = 0, sat;
            string name;
            Console.WriteLine("Escriba el nombre del dinosaurio a buscar");
            name = Console.ReadLine();
            for (core = 0; core < woke.Length; core++)
            {
                if (name == woke[core].name)
                {
                    Console.WriteLine("Especie\t\tNombre\t\tCosto de Habitat\t\tPlan de Alimentación\t\tCosto Comida Mensual");
                    Console.Write(woke[core].esp + "\t\t" + woke[core].name + "\t\t$" + (woke[core].largo * 269 * 6.9) + "\t\t");
                    for (sat = 0; sat < 4; sat++)
                    {
                        Console.Write(woke[core].dieta[sat] + " ");
                    }
                    Console.Write("\t\t$" + woke[core].costo);
                    Console.WriteLine("");
                    fake = 1;
                }
            }

            if (fake == 0)
                Console.WriteLine("No existe un dinosaurio con ese nombre");
        }
        static void calc(dino[] arg)//función que regresa la inversión mientras el usuario mande dentro de cuantos años desea.
        {
            int años;
            Console.WriteLine("Escriba los años a estimar la inversión");
            años = int.Parse(Console.ReadLine());
            Console.WriteLine("Ganancia estimada en " + años + " años: $" + ((invi(arg) + mens(arg)) * .47 * años));
        }
        static void finder(dino[] sharp) //contador de dinosaurios por el tipo de dieta.
        {
            int herb = 0, carn = 0, car;
            for (car = 0; car < sharp.Length; car++)
            {
                if (sharp[car].especie <= 5)
                    carn = carn + 1;
                else
                    herb = herb + 1;
            }
            Console.WriteLine("Dinosaurios Carnívoros: " + carn);
            Console.WriteLine("Dinosaurios Herbívoros: " + herb);
        }
        static void vary(dino[] siete)//buscar el dinosaurio que costó más y el dinosaurio que costó menos.
        {
            int code, max = 0, min = 0, cad;
            double maxmed = 0, minmed = 0;
            for (code = 0; code < siete.Length; code++)
            {
                if (code == 0)
                {
                    min = code;
                    minmed = siete[code].costo + siete[code].largo;
                    max = code;
                    maxmed = siete[code].costo + siete[code].largo;
                }
                else if ((siete[code].costo + siete[code].largo) > maxmed)
                {
                    max = code;
                    maxmed = siete[code].costo + siete[code].largo;
                }
                else if ((siete[code].costo + siete[code].largo) < minmed)
                {
                    min = code;
                    minmed = siete[code].costo + siete[code].largo;
                }

            }//imprimir la tabla de dinosaurios que costó más 
            Console.WriteLine("Dinosaurio de Gastos Mínimos");
            Console.WriteLine("Especie\t\tNombre\t\tCosto de Habitat\t\tPlan de Alimentación\t\tCosto Comida Mensual");
            Console.Write(siete[min].esp + "\t\t" + siete[min].name + "\t\t$" + (siete[min].largo * 269 * 6.9) + "\t\t");
            for (cad = 0; cad < 4; cad++)
            {
                Console.Write(siete[min].dieta[cad] + " ");
            }
            Console.Write("\t\t$" + siete[min].costo);
            Console.WriteLine("");
            Console.WriteLine("");
            Console.WriteLine("Dinosaurio de Gastos Máximos");
            Console.WriteLine("Especie\t\tNombre\t\tCosto de Habitat\t\tPlan de Alimentación\t\tCosto Comida Mensual");
            Console.Write(siete[max].esp + "\t\t" + siete[max].name + "\t\t$" + (siete[max].largo * 269 * 6.9) + "\t\t");
            for (cad = 0; cad < 4; cad++)
            {
                Console.Write(siete[max].dieta[cad] + " ");
            }
            Console.Write("\t\t$" + siete[max].costo);
            Console.WriteLine("");
        }
        static void gt(dino[] adiós)//calcular el costo de boleto para que los inversionistas obtengan un 47% de ganancia, usando el hecho de que cada dinosaurio obtendrá 3.2 millones de personas anualmente 
        {
            Console.WriteLine("Costo de boleto: $" + ((invi(adiós) + mens(adiós)) * 1.47) / (adiós.Length * 3200000));
        }
        static void Main(string[] args)// el Main, donde se encuentra el menú principal, está estructurado a base de funciones
        {
            int n, opción;
            char resp;

            Console.Clear();
            do
            {
                Console.WriteLine("¿Cuantos dinosaurios va a tener su parque?");
                n = int.Parse(Console.ReadLine());
                if (n < 3 || n > 45)
                    Console.WriteLine("Debe haber un minimo de 3 dinosaurios y un maximo de 45");
            } while (n < 3 || n > 45);
            dino[] danonino = new dino[n];
            Llenado(danonino);
            do
            {
                Console.WriteLine("Bienvenido Al Menú de Opción:");
                Console.WriteLine("1.- Inversión Inicial:");
                Console.WriteLine("2.- Tabla de costos Mensuales:");
                Console.WriteLine("3.- Inversión para el primer año:");
                Console.WriteLine("4.- Búsqueda de dinosaurios por nombre:");
                Console.WriteLine("5.- Contador de dinosaurios herbívoros y carnívoros:");
                Console.WriteLine("6.- Calcular la ganancia");
                Console.WriteLine("7.- Dinosaurio de mínimo y máximo costo");
                Console.WriteLine("8.- Costo del boleto para ganancia del 47%");
                opción = int.Parse(Console.ReadLine());
                switch (opción)
                {
                    case 1:
                        {
                            Console.WriteLine("Inversión Inicial: $" + invi(danonino));
                            break;
                        }
                    case 2:
                        {
                            imprimir(danonino);
                            break;
                        }
                    case 3:
                        {
                            Console.WriteLine("Inversión Total: $" + (invi(danonino) + mens(danonino)));
                            break;
                        }
                    case 4:
                        {
                            buscar(danonino);
                            break;
                        }
                    case 5:
                        {
                            finder(danonino);
                            break;
                        }
                    case 6:
                        {
                            calc(danonino);
                            break;
                        }
                    case 7:
                        {
                            vary(danonino);
                            break;
                        }
                    case 8:
                        {
                            gt(danonino);
                            break;
                        }
                    default:
                        {
                            Console.WriteLine("La opción seleccionada no existe.");
                            break;
                        }
                }
                Console.WriteLine("¿Desea seleccionar otra opción? (s/n)");
                resp = char.Parse(Console.ReadLine());
            } while (resp == 'S' || resp == 's');
        }
    }
}
