public class Mobile_Members extends Integrantes {

    public Mobile_Members(String nome, String email) {
        super(nome, email, "Mobile Members");
        
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("Happy_C0d1ng. Maskers");
        else System.out.println("Happy Coding!");
        return null;
    }
    
    
}
