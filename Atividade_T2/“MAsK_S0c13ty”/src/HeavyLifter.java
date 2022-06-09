public class HeavyLifter extends Integrantes{

    public HeavyLifter(String nome, String email) {
        super(nome, email, "HeavyLifter");
        
    }

    @Override
    public String PostarMensagem(String status) {
        if (status == "Atividade Extra")
            System.out.println("N00b_qu3_n_Se_r3pita.bat");
        else System.out.println("Podem contar conosco!");
        return null;
    }
    
    
}
