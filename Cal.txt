#!/bin/bash



echo "Olá, esse é um projeto de calculadora em desenvolvimento, se atente às orientações!"
echo ""
echo "Para utilizar essa calculadora:"
echo "- Informe um número e aperte 'Enter'"
echo "- Escolha uma operação (+, -, /, *) e aperte 'Enter'"
echo "- Informe o segundo número e aperte 'Enter' novamente"
echo "- Aguarde enquanto o cálculo é realizado!"
echo "Vamos começar!!!"
echo ""


cont_cal="s"

while [[ "$cont_cal" == "s" ]]; do
    echo ""
    read -p "Informe o primeiro valor que deseja calcular: " valor1
    read -p "Informe a operação que deseja realizar (+, -, /, *): " operacao
    read -p "Informe o segundo valor que deseja calcular: " valor2

    
    if ! [[ "$valor1" =~ ^[0-9]+(\.[0-9]+)?$ ]] || ! [[ "$valor2" =~ ^[0-9]+(\.[0-9]+)?$ ]]; then
        echo "Erro: Certifique-se de inserir números válidos."
        continue
    fi

    
    case "$operacao" in
        "+")
            resposta=$(echo "$valor1 + $valor2" | bc)
            echo "$valor1 + $valor2 = $resposta"
            ;;
        "-")
            resposta=$(echo "$valor1 - $valor2" | bc)
            echo "$valor1 - $valor2 = $resposta"
            ;;
        "/")
            if [ "$valor2" != "0" ]; then
                resposta=$(echo "scale=2; $valor1 / $valor2" | bc)
                echo "$valor1 / $valor2 = $resposta"
            else
                echo "Erro: divisão por zero não é permitida."
            fi
            ;;
        "*")
            resposta=$(echo "$valor1 * $valor2" | bc)
            echo "$valor1 * $valor2 = $resposta"
            ;;
        *)
            echo "Operação inválida! Tente novamente usando +, -, / ou *."
            ;;
    esac

    read -p "Deseja realizar outro cálculo? (s/n): " cont_cal
    cont_cal=$(echo "$cont_cal" | tr '[:upper:]' '[:lower:]')  # converte para minúsculas

    if [[ "$cont_cal" == "n" ]]; then
        echo "Obrigada por utilizar nossos serviços, até a próxima!"
        break
    fi
done
