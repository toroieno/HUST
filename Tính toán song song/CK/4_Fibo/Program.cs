using System;
using Alchemi.Core.Owner;

namespace FiboNumber
{
    class FiboNumber : GApplication
    {
        public static GApplication App = new GApplication();
        private static int NumPerThread;//So luong so trong 1 thread
        private static DateTime start;

        [STAThread]
        static void Main(string[] args)
        {
            Console.OutputEncoding = System.Text.Encoding.UTF8;
            Console.WriteLine("BÀI TẬP FIBONACCI");
            Console.Write("Nhập: n = ");
            int n = Int32.Parse(Console.ReadLine());
            Console.Write("Đưa vào số luồng cho 1 thread: ");
            NumPerThread = Int32.Parse(Console.ReadLine());
            
            Console.WriteLine();
            int NumRemain = n;
            int NumCur = 1;
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

                App.Threads.Add(new FiboNumberCheck(Begin, End));
                NumRemain -= NumberOfThread;
            }
            App.Connection = new GConnection("localhost", 9000, "user", "user");
            App.Manifest.Add(new ModuleDependency(typeof(FiboNumberCheck).Module));
            App.ThreadFinish += new GThreadFinish(App_ThreadFinish);
            App.ApplicationFinish += new GApplicationFinish(App_ApplicationFinish);
            start = DateTime.Now;
            Console.WriteLine("Thread started!");
            App.Start();
            Console.ReadLine();

        }

        private static void App_ThreadFinish(GThread thread)
        {
            FiboNumberCheck fnc = (FiboNumberCheck)thread;
            Console.Write("tính {0}-{1} hoàn thành: ", fnc.Begin, fnc.End);
            for (int i = fnc.Begin; i <= fnc.End; i++)
            {
                Console.Write( fnc.Fibos[i] + " ");
            }
            Console.WriteLine();
        }
        private static void App_ApplicationFinish()
        {
            Console.WriteLine("Hoàn thành sau {0} seconds.", DateTime.Now - start);
        }
    }
    [Serializable]
    class FiboNumberCheck : GThread
    {
        public int Begin, End;
        public long[] Fibos = new long[100];
        public FiboNumberCheck(int begin, int end)
        {
            this.Begin = begin;
            this.End = end;
        }
        private long Fibo(int m) // Direct Calculation, correct for abs(m) <= 92
        {
            double s = 1.0 / Math.Sqrt(5.0);
            double g1 = (1.0 + Math.Sqrt(5.0)) / 2.0;
            double g2 = (1.0 - Math.Sqrt(5.0) / 2);
            return (long)Math.Round(s * (Math.Pow(g1, m) - Math.Pow(g2, m)));
        }
        public override void Start()
        {
            for (int i = Begin; i <= End; i++)
            {
                Fibos[i] = Fibo(i);
            }
        }
    }
}
