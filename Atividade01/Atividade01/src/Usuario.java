// Matheus Marins Bernardello
// RA: 20.00286-6 

public class Usuario {
    private String nome;
    private Bens bens;
    
    
    public Usuario(String nome) {
        this.nome = nome;
        this.bens = new Bens();
    }
   
    @Override
    public String toString() {
        return "Usuario [bens=" + bens + ", nome=" + nome + "]";
    }


    public String getNome() {
        return nome;
    }


    public Bens getBens() {
        return bens;
    }

    public static EmprestarBem(){

    }

}
