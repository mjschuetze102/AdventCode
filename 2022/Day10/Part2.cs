using System;
using System.Collections.Generic;

namespace AdventOfCode.Day10
{
    class Part2
    {
        class Instruction
        {
            private int _ticksToComplete;
            private int _ticksRemaining;
            private int _value;

            public Instruction(int ticksToComplete)
            {
                _ticksToComplete = ticksToComplete;
            }

            public void Start(int value)
            {
                _ticksRemaining = _ticksToComplete;
                _value = value;
            }

            public bool HasTicksRemaining()
            {
                return _ticksRemaining > 0;
            }

            public int Tick()
            {
                _ticksRemaining--;
                if (_ticksRemaining == 0) return _value;

                return 0;
            }
        }

        class Noop : Instruction
        {
            public Noop() : base(1) { }
        }

        class Addx : Instruction
        {
            public Addx() : base(2) { }
        }

        private static Dictionary<string, Instruction> instructionMatrix = new Dictionary<string, Instruction> {
            { "noop", new Noop() },
            { "addx", new Addx() },
        };

        static void Temp()
        {
            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\User\Downloads\advent.txt");

            int ticks = 0;
            int register = 1;
            foreach (string line in lines)
            {
                string[] instruction = line.Split(" ");
                instructionMatrix[instruction[0]].Start(instruction.Length > 1 ? Int32.Parse(instruction[1]) : 0);

                for (; instructionMatrix[instruction[0]].HasTicksRemaining(); register += instructionMatrix[instruction[0]].Tick())
                {
                    ticks++;
                    Console.Write(Math.Abs(register - ((ticks - 1) % 40)) <= 1 ? "#" : ".");
                    if (ticks % 40 == 0) Console.WriteLine();
                }
            }
        }
    }
}
