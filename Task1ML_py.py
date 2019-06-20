{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Task1ML.py",
      "version": "0.3.2",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/starcyultron/summer19ML/blob/master/Task1ML_py.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "IrDOYODhJyIF",
        "colab_type": "code",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 54
        },
        "outputId": "397193f7-8f48-4f1d-ad14-e6f22c720296"
      },
      "source": [
        "import numpy as np\n",
        "import random\n",
        "import csv\n",
        "m=int(input(\"Enter no. of rows : \"))\n",
        "n=int(input(\"Enter no. of column : \"))\n",
        "p=np.random.random((m,n))\n",
        "p\n",
        "with open(\"new_file.csv\",\"w+\") as my_csv:\n",
        "    csvWriter = csv.writer(my_csv,delimiter=',')\n",
        "    csvWriter.writerows(p)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Enter no. of rows : 4\n",
            "Enter no. of column : 6\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "-K5EXw-nMcpb",
        "colab_type": "code",
        "colab": {}
      },
      "source": [
        ""
      ],
      "execution_count": 0,
      "outputs": []
    }
  ]
}
