using System;
using System.Linq;

namespace AdventOfCode.Day6
{
    class Part1
    {
        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");
            
            foreach (string line in lines)
            {
                for (int i = 0; i < line.Length - 5; i++)
                {
                    if (line.Substring(i, 4).Distinct().Count() == 4)
                    {
                        Console.WriteLine(i + 4);
                        break;
                    }
                }
            }
        }
    }
}
