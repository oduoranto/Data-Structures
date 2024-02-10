//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {

        int[] arrayNum;
        arrayNum = new int[] {1,3,78,85,89};

        System.out.println(arrayNum.length);

        for (int i = 0; i < arrayNum.length ; i ++){

            System.out.print(arrayNum[i] + " ");
        }
        System.out.println();

        for (int element : arrayNum){

            System.out.print(element + " ");
        }
      

    }

}