class Largest
{
    public static void main(String a[])
    {
        int a1=90,a2=79,a3=86;
        int l1=0,l2=0;
        if(a1>a2 && a2>a3){
            l1=a1;
            l2=a2;}
        else if(a2>a3 && a2>a1 && a3>a1){
          l1=a2;
            l2=a3;}
        else
            l2=a3;
            l1=a2;
        System.out.println(l1+l2);



    }
}