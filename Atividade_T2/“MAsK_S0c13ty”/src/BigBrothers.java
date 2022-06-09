public class BigBrothers extends Integrantes {

    public BigBrothers(String nome, String email) {
        super(nome, email, "BigBrother");
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("...");
        else System.out.println("Sempre ajudando as pessoas membros ou não S2!");
        return null;
    }
    
}
