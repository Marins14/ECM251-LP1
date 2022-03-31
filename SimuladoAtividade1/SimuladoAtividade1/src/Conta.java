public class Conta {
    // atributos da nossa classe
    private String idConta;
    private double saldo;
    private Usuario usuario;
    

    public Conta(Usuario usuario,String idConta){
        this.idConta = idConta;
        this.usuario = usuario;
        saldo = 0;

    }
    
    // Métodos da classe 

    public void visualizarSaldo(){
    System.out.println("Id da Conta" +idConta + ": Quanto tem disponivel: R$ " +this.saldo);
    }
    public boolean depositar(double valor){
       if(valor < 0) return false;
       this.saldo += valor; 
       return true;
       

    }
    public boolean sacar(double valor){
        if(valor>saldo) return false;
        if(valor< 0) return false;
        this.saldo -= valor;
        return true;

    }
    public boolean transferirDinheiro(double valor, Conta destino){
        if(!this.sacar(valor)) return false;

        if(!destino.depositar(valor)) return false;
        return true;


    }


}
