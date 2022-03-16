public class Conta {
    // atributos da nossa classe
    int numero;
    String titular;
    double saldo;
    String cpf;

    // Métodos da classe 

    void visualizarSaldo(){
        System.out.println("Saldo atual na conta" +numero + ": R$ " +this.saldo);
    }
    void depositar(double valor){
        if(valor>0){
            saldo = saldo + valor;

        }

    }
    void sacar(double valor){
        if(valor<=saldo){
            saldo = saldo - valor;
        }    
    }
    void transferirDinheiro(){}


}
