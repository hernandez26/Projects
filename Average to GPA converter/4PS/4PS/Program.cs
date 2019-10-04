using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

//Jonathan Hernandez
// Chapter 7 & 8 Homework
//
//(Converting Grade Averages to a Four-Point Scale) 
//Write method QualityPoints that inputs a student’s average and returns 4 if the student's average is 90–100, 
//3 if the average is 80–89, 2 if the average is 70–79, 1 if the average is 60–69 and 0 if the average is lower than 60. 
//Incorporate the method into an app that reads a value from the user and displays the result.

namespace _4PS
{
    class Program
    {
        static void Main(string[] args)
        {
            //Here the program asks for a grade average in order to determine the GPA.
            Console.WriteLine("Enter your grade average to determine your GPA: ");

            //Here the program takes the number returned from the function QualityPoints and stores it into the variable named GPA. This is the Calculated GPA.
            var GPA = QualityPoints(Convert.ToInt32(Console.ReadLine()));

            //Here the program outputs the GPA result.
            Console.WriteLine("Your GPA is {0:F}",GPA) ;

            Console.ReadKey();
        }

        /// <summary>
        /// This function uses If statements to determine what the students GPA is.
        /// </summary>
        /// <param name="grade"></param>
        /// <returns></returns>
        public static Double QualityPoints(int grade)
        {
            if (grade >= 90 && grade <= 100)
            {
                return 4.0;
            }
            else if (grade >= 80 && grade <= 89)
            {
                return 3.0;
            }
            else if (grade >= 70 && grade <= 79)
            {
                return 2.0;
            }
            else if (grade >= 60 && grade <= 69)
            {
                return 1.0;
            }
            else
                return 0;


        }

    }
}
