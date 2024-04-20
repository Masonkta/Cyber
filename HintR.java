import java.lang.reflect.*;

public class HintR {
    public static void main(String[] args) throws Exception
    {
        Hint h = new Hint();
        Class c = h.getClass();

        System.out.println("The superclass is " + c.getSuperclass().getName());
        System.out.println("the name of the class is " + c.getName());

        Method[] methods = c.getMethods();
        for (Method m : methods){
            System.out.println(m);
        }

        System.out.println("------------------------------------------------------------------");

        Method[] allmethods = c.getDeclaredMethods();
        for (Method m : allmethods)
            System.out.println(m);

        Method m1 = c.getDeclaredMethod("setLength", int.class);
        m1.invoke(h, 1000);

        Method m2 = c.getDeclaredMethod("superprivatefunction");
        m2.setAccessible(true);
        m2.invoke(h);
    }
}