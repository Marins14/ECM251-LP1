// Matheus Marins Bernardello
// RA: 20.00286-6
import java.util.concurrent.ThreadLocalRandom;

public class Bens {
    private int idBem = 0;
    private String Tipo;
      

    public  String geraridBem(int idBem, String tipo){
        this.idBem = ThreadLocalRandom.current().nextInt(0,6);
        this.Tipo = tipo;
        return geraridBem(idBem, tipo);
            
    }

    
    public int getIdBem() {
        return idBem;
    }
    public String getTipo() {
        return Tipo;
    }
    public String testar(){
        return String.format("%d;%s", idBem ,Tipo);
  

    }     
}
