using System;

namespace AdventOfCode
{
    class Part1
    {
        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");

            int currCalories = 0;
            int mostCalories = 0;
            foreach (string line in lines)
            {
                if (line == "")
                {
                    if (currCalories > mostCalories) mostCalories = currCalories;

                    currCalories = 0;
                    continue;
                }

                currCalories += Int32.Parse(line);
            }

            if (currCalories > mostCalories) mostCalories = currCalories;

            Console.WriteLine($"Calories: {mostCalories}");
        }
    }
}
