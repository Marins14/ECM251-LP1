public class Usuario {
    private String nome;
    private String senha;
    private String email;
    // conta dentro do cliente 
    



    public  Usuario(String nome, String senha, String email){
        this.nome = nome;
        this.senha = senha;
        this.email = email;
        

    }

    public void visualizarUsuario(){
        System.out.println("Dados do usuario:");
        System.out.println("Nome:" +nome);
        System.out.println("email:" +email);
        
    }
    public String getNome(){
        return nome;
    }
     
    public String getEmail(){
        return email;
    }
       
}
