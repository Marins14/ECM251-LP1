import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

public class Sistema {
    public static void rodar(){
        String status;
        int sorteio = ThreadLocalRandom.current().nextInt(0,2);
        if(sorteio == 1)
            status = "Atividade Regular";
        else status = "Atividade Regular";
        
            
        List<Integrantes> MAsK_S0c13ty = new ArrayList<Integrantes>();
        MAsK_S0c13ty.add(new HeavyLifter("JOs3", "joseidopapis@lolzin.br"));
        MAsK_S0c13ty.add(new Mobile_Members("J3SyC4", "Program@theWitcher.com"));
        MAsK_S0c13ty.add(new BigBrothers("Y33N33F3R", "Trissnaopassara@geralt.com"));
        MAsK_S0c13ty.add(new Scripty_Guys("T4i$$", "DesistoDaYennefer@geralemeu.com.br")); 
        
        mudarTurno(status);
        mostraIntegrantes(MAsK_S0c13ty);
    }

    public static void mudarTurno(String status){
        if (status != "Atividade Regular")
            status = "Atividade Extra";
        else status = "Atividade Regular";
    }
    public static void mostraIntegrantes(List<Integrantes> MAsk_S0c13ty){
        for (Integrantes integrantes : MAsk_S0c13ty) {
            System.out.println(integrantes);
        }
    }
}