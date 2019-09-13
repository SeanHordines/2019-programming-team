import java.util.*;
import java.io.*;

public class chinese
{
    static int startYr = 1965;
    static String[] zodiac = {"snake", "horse", "sheep", "monkey", "rooster", "dog", "pig", "rat", "ox", "tiger", "rabbit", "dragon"};

    public static void main(String[] args) throws IOException {
        Scanner in = new Scanner(System.in);
        int t = in.nextInt();

        for (int i = 0; i < t; i++){
            int temp = in.nextInt();
            System.out.println( temp + " is the year of the " + zodiac[findSign(temp)]);
        }
    }

    public static int findSign(int year){
        return ((year - startYr) % 12);
    }
}
