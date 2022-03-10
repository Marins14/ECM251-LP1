public class Caneta {
    String modelo;
    String cor;
    int carga;
    double ponta;
    final int CARGA_INICIAL = 100;

    void iniciarCaneta(String cor, String modelo, double ponta) {
        this.cor = cor;
        this.modelo = modelo;
        this.ponta = ponta;
        this.carga = CARGA_INICIAL;

    }

    void escrever(String texto) {
        for (int i = 0; i < texto.length(); i++) {
            if(this.carga >0){
                System.out.print(texto.charAt(i));
                this.carga -= 1;
            }else{
                System.out.print("\nCaneta SEM Carga caraio");
                break;
            }
        }        
    }        
    //     }
    //     if(texto.length() > this.carga)
    //         System.out.println("Caneta SEM Carga caraio");

    //     else {
    //         System.out.println(texto);
    //         this.carga -= texto.length();
            
    //     }
    // }

    String mostrarDados(){
                return "Modelo: " + this.modelo +
                        " - Cor: " + this.cor +
                        " - Ponta: " + this.ponta +
                        " - Carga: " + this.carga; 
    }

}
