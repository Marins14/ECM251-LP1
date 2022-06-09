public class Integrantes implements PostarMensagem {
    public final String nome;
    public final String email;
    public final String funcao;

    public Integrantes(String nome, String email, String funcao) {
        this.nome = nome;
        this.email = email;
        this.funcao = funcao;
    }


    @Override
    public String toString() {
        return "Integrantes [email=" + email + ", funcao=" + funcao + ", nome=" + nome + "]";
    }


    @Override
    public String PostarMensagem(String Status) {
        
        return null;
    }
    
}
