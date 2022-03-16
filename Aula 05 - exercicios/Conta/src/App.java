public class App {
    public static void main(String[] args) throws Exception {
        //Declara um objeto do tipo conta
        Conta minhaConta;
        // Instanciar um objeto do tipo conta
        minhaConta = new Conta();
        // Declarou e instanciou um objeto do tipo conta
        Conta outraConta = new Conta();

        minhaConta.saldo = 200.0;
        minhaConta.numero = 12345;
        outraConta.saldo = 150.0; 
        outraConta.numero = 4563;

        System.out.println("Saldo na minhaConta: ");
        minhaConta.visualizarSaldo();
        System.out.println("Saldo na minhaConta: ");
        outraConta.visualizarSaldo();

        minhaConta.depositar(-500.00);
        minhaConta.sacar(2100.00);
        minhaConta.visualizarSaldo();
    }
}
