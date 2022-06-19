
import java.util.Scanner;
/**
 * names
 */
public class names {

    public static void main(String[] args) {
       //an array which stores the names of the students
       Scanner input = new Scanner(System.in);
       System.out.print("enterr number of students you want to enter:");
       int number=input.nextInt();
        String[] names = new String[number];
        for(int i=0;i<number;i++){
            System.out.print("enter the name of the student:");
            names[i]=input.next();

        }
        //ask the user if the want to remove a student
        System.out.print("do you want to remove a student?(y/n)");
        String answer=input.next();
        if(answer.equals("y")){
            System.out.print("enter the name of the student you want to remove:");
            String name=input.next();
            for(int i=0;i<number;i++){
                if(names[i].equals(name)){
                    names[i]=names[number-1];
                    number--;
                }
            }
        }
        //print the names of the remaning students
        for(int i=0;i<number;i++){
            System.out.println(names[i]);
        }
        //ask the user if the want to add a student
        System.out.print("do you want to add a student?(y/n)");
        answer=input.next();
        if(answer.equals("y")){
            System.out.print("enter the name of the student you want to add:");
            String name=input.next();
            names[number]=name;
            number++;
        }
        for(int i=0;i<number;i++){
            System.out.println(names[i]);
        }
    }
}