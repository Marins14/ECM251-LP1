public class Scripty_Guys extends Integrantes {

    public Scripty_Guys(String nome, String email) {
        super(nome, email, "Scripty Guys");
        
    }
    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("QU3Ro_S3us_r3curs0s.py");
        else System.out.println("Prazer em ajudar novos amigos de código!");
        return null;
    }
    
}
