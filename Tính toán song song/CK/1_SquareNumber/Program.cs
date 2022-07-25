using System;
using Alchemi.Core.Owner;

namespace SquareNumber
{
    class SquareNumber : GApplication
    {
        public static GApplication App = new GApplication();
        private static bool[] matrix;//Mang chua so can kiem tra
        private static int NumPerThread;//So luong so trong 1 thread
        private static DateTime start;
     
        [STAThread]
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("BÀI TẬP TÌM SỐ CHÍNH PHƯƠNG");
            Console.Write("Nhập: n = ");
            int n = Int32.Parse(Console.ReadLine());
            Console.Write("Đưa vào số luồng cho 1 thread: ");
            NumPerThread = Int32.Parse(Console.ReadLine());
            matrix = new bool[n+1];
            for (int i = 0; i <= n; i++)
            {
                matrix[i] = false;
            }
            Console.WriteLine();
            int NumRemain = n;
            int NumCur = 0;
            int NumberOfThread, Begin, End;
            while (NumRemain > 0)
            {
                if (NumRemain > NumPerThread)
                {
                    NumberOfThread = NumPerThread;
                }
                else
                {
                    NumberOfThread = NumRemain;
                }
                Begin = NumCur;
                NumCur += NumberOfThread;
                if (NumCur >= n) { End = n; }
                else { End = NumCur - 1; }
                
                App.Threads.Add(new SquareNumberCheck(Begin, End, matrix));
                NumRemain -= NumberOfThread;
            }
            App.Connection = new GConnection("localhost",9000,"user","user");
            App.Manifest.Add(new ModuleDependency(typeof(SquareNumberCheck).Module));
            App.ThreadFinish += new GThreadFinish(App_ThreadFinish);
            App.ApplicationFinish += new GApplicationFinish(App_ApplicationFinish);
            start = DateTime.Now;
            Console.WriteLine("Thread started!");
            App.Start();
            Console.ReadLine();

        }

        private static void App_ThreadFinish(GThread thread)
        {
            SquareNumberCheck snc = (SquareNumberCheck)thread;
            Console.Write("Kiểm tra {0}-{1} hoàn thành: ", snc.Begin, snc.End);
            for (int i = snc.Begin; i <= snc.End; i++)
                if (snc.Snumbers[i] == true) Console.Write(i + " ");
            Console.WriteLine();
        }

        private static void App_ApplicationFinish()
        {
            Console.WriteLine("Hoàn thành sau {0} seconds.",DateTime.Now-start);
        }
    }
    [Serializable]
    class SquareNumberCheck : GThread
    {
        public int Begin, End;
        public bool[] Snumbers;
        public SquareNumberCheck(int begin, int end, bool[] numbers)
        {
            this.Begin = begin;
            this.End = end;
            this.Snumbers = numbers;
        }
        public override void Start()
        {
            for (int i = Begin; i <= End; i++)
            { 
                if (Math.Sqrt(i) == (int)(Math.Sqrt(i)))
                {
                    Snumbers[i] = true;
                }
            }
        }
    }
}
