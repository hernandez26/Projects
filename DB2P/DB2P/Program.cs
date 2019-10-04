using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//  Jonathan Hernandez
// Homework Chapter 7 & 8 Homework
//
//(Distance Between Two Points) Write method Distance to calculate the distance betweentwo points(x1, y1) and(x2, y2). 
//All numbers and return values should be of type double. 
//Incorporat ethis method into an app that enables the user to enter the coordinates of the points.

namespace DB2P
{
    class Program
    {
        static void Main(string[] args)
        {
            // Here the program prompts the user for the first X input.
            Console.WriteLine("Enter X1: ");
            // Here the program reads the inputs
            var X1 = Convert.ToDouble(Console.ReadLine());
           
            // Here the program prompts the user for the first Y input.
            Console.WriteLine("Enter Y1: ");
            // Here the program reads the input
            var Y1 = Convert.ToDouble(Console.ReadLine());

            // Here the program prompts the user for the second X input.
            Console.WriteLine("Enter X2: ");
            // Here the program reads the inputs
            var X2 = Convert.ToDouble(Console.ReadLine());


            // Here the program prompts the user for the second X input.
            Console.WriteLine("Enter Y2: ");
            // Here the program reads the inputs
            var Y2 = Convert.ToDouble(Console.ReadLine());

            // Here Main call the Calculation function to calculate the result. The result is then stored in the variable named Outcome.
            var Outcome = Calculation(X1, X2, Y1, Y2);

            // Here the program prints the result.
            Console.WriteLine("Distance between coordinates {0}, {1}, and {2}, {3} is:  {4}", X1, Y1, X2, Y2, Outcome);

            Console.ReadKey();

        }
        /// <summary>
        /// This function calculates the distance between the 2 points.
        /// </summary>
        /// <param name="X1"></param>
        /// <param name="X2"></param>
        /// <param name="Y1"></param>
        /// <param name="Y2"></param>
        /// <returns></returns>
        private static double Calculation(double X1, double X2, double Y1, double Y2)
        {
            //  The First X is subtracted from the second X and then raised to the 2 power. This is then stored in MinusX.
            var MinusX = Math.Pow((X2 - X1), 2);
            
            //  The First Y is subtracted from the second Y and then raised to the 2 power. This is then stored in MinusY.
            var MinusY = Math.Pow((Y2 - Y1), 2);
            
            // X and Y are them added and stored into XplusY
            var XplusY = Math.Sqrt(MinusX+ MinusY);

            return XplusY;
        }
    }
}




