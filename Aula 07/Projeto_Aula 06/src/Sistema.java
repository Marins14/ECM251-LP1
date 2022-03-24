public class Sistema {
    public void run(){
        Cliente cliente = new Cliente("Geralt", "123658", "ciri_yennefer@gmail.com");
        Conta conta = new Conta(cliente, 1234);
        System.out.println(conta);
        
    }
}
