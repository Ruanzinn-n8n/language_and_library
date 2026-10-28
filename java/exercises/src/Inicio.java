public class Inicio {
    String name;
    int camisa;

    public Inicio(String name, int camisa) {
        this.name = name;
        this.camisa = camisa;
    }

    public void exibirDados(){
        System.out.println("\n-----------------------------");
        System.out.println("Jogador: " + name);
        System.out.println("Camisa: " + camisa);
        System.out.println("-----------------------------");
    }

    public static void main(String[] args) {
        Inicio jogador1 = new Inicio("Ruan", 10);
        Inicio jogador2 = new Inicio("Lucas", 15);

        System.out.println("=========== TIME ============");
        jogador1.exibirDados();
        jogador2.exibirDados();
    }
}
