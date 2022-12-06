using System;
using System.Linq;

namespace AdventOfCode.Day6
{
    class Part2
    {
        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");

            foreach (string line in lines)
            {
                for (int i = 0; i < line.Length - 15; i++)
                {
                    if (line.Substring(i, 14).Distinct().Count() == 14)
                    {
                        Console.WriteLine(i + 14);
                        break;
                    }
                }
            }
        }
    }
}
