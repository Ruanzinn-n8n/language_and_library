public class Main {
    public static void main(String[] args) {
        String red = "\u001B[31m";
        String black = "\u001B[30m";
        String reset = "\u001B[0m";

        String[] card = {
                "┌───────┐",
                "│ A     │",
                "│   ♥   │",
                "│     A │",
                "└───────┘"};

        for (String linha : card){
            System.out.println(linha);
        }

    }
}
