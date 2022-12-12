{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1kqilNTPP6sFhRipZJKqog8tewxQ9ymez",
      "authorship_tag": "ABX9TyPwJJKYblPXts4Ab1CBT9wN"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "bTs3bZxmn4HQ",
        "outputId": "b7e54e32-012f-4b93-d0f0-3cbfb6ecad44"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.15.2-py2.py3-none-any.whl (9.2 MB)\n",
            "\u001b[K     |████████████████████████████████| 9.2 MB 5.1 MB/s \n",
            "\u001b[?25hRequirement already satisfied: click>=7.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (7.1.2)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (2.23.0)\n",
            "Collecting gitpython!=3.1.19\n",
            "  Downloading GitPython-3.1.29-py3-none-any.whl (182 kB)\n",
            "\u001b[K     |████████████████████████████████| 182 kB 54.2 MB/s \n",
            "\u001b[?25hRequirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (5.2.0)\n",
            "Collecting pydeck>=0.1.dev5\n",
            "  Downloading pydeck-0.8.0-py2.py3-none-any.whl (4.7 MB)\n",
            "\u001b[K     |████████████████████████████████| 4.7 MB 32.3 MB/s \n",
            "\u001b[?25hRequirement already satisfied: altair>=3.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.2.0)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.8/dist-packages (from streamlit) (0.10.2)\n",
            "Collecting validators>=0.2\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.8/dist-packages (from streamlit) (3.19.6)\n",
            "Collecting semver\n",
            "  Downloading semver-2.13.0-py2.py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.13.0)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (4.4.0)\n",
            "Collecting watchdog\n",
            "  Downloading watchdog-2.2.0-py3-none-manylinux2014_x86_64.whl (78 kB)\n",
            "\u001b[K     |████████████████████████████████| 78 kB 4.0 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (7.1.2)\n",
            "Collecting rich>=10.11.0\n",
            "  Downloading rich-12.6.0-py3-none-any.whl (237 kB)\n",
            "\u001b[K     |████████████████████████████████| 237 kB 49.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.5.1)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.8/dist-packages (from streamlit) (21.3)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.21.6)\n",
            "Requirement already satisfied: tornado>=5.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (6.0.4)\n",
            "Collecting pympler>=0.9\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[K     |████████████████████████████████| 164 kB 47.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: pandas>=0.21.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (1.3.5)\n",
            "Collecting blinker>=1.0.0\n",
            "  Downloading blinker-1.5-py2.py3-none-any.whl (12 kB)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.8/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (0.12.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.8/dist-packages (from altair>=3.2.0->streamlit) (4.3.3)\n",
            "Collecting gitdb<5,>=4.0.1\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[K     |████████████████████████████████| 62 kB 823 kB/s \n",
            "\u001b[?25hCollecting smmap<6,>=3.0.1\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.8/dist-packages (from importlib-metadata>=1.4->streamlit) (3.11.0)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (22.1.0)\n",
            "Requirement already satisfied: importlib-resources>=1.4.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (5.10.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.8/dist-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.19.2)\n",
            "Requirement already satisfied: pyparsing!=3.0.5,>=2.0.2 in /usr/local/lib/python3.8/dist-packages (from packaging>=14.1->streamlit) (3.0.9)\n",
            "Requirement already satisfied: pytz>=2017.3 in /usr/local/lib/python3.8/dist-packages (from pandas>=0.21.0->streamlit) (2022.6)\n",
            "Requirement already satisfied: MarkupSafe>=0.23 in /usr/local/lib/python3.8/dist-packages (from jinja2->altair>=3.2.0->streamlit) (2.0.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.8/dist-packages (from python-dateutil->streamlit) (1.15.0)\n",
            "Requirement already satisfied: urllib3!=1.25.0,!=1.25.1,<1.26,>=1.21.1 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (1.24.3)\n",
            "Requirement already satisfied: chardet<4,>=3.0.2 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (3.0.4)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2022.9.24)\n",
            "Requirement already satisfied: idna<3,>=2.5 in /usr/local/lib/python3.8/dist-packages (from requests>=2.4->streamlit) (2.10)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.6.0 in /usr/local/lib/python3.8/dist-packages (from rich>=10.11.0->streamlit) (2.6.1)\n",
            "Collecting commonmark<0.10.0,>=0.9.0\n",
            "  Downloading commonmark-0.9.1-py2.py3-none-any.whl (51 kB)\n",
            "\u001b[K     |████████████████████████████████| 51 kB 1.7 MB/s \n",
            "\u001b[?25hRequirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.8/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19581 sha256=d0bd68aa4bbb663cc85c3ca99309e04f72074d62ca17047404c84cd7124a9b9a\n",
            "  Stored in directory: /root/.cache/pip/wheels/19/09/72/3eb74d236bb48bd0f3c6c3c83e4e0c5bbfcbcad7c6c3539db8\n",
            "Successfully built validators\n",
            "Installing collected packages: smmap, gitdb, commonmark, watchdog, validators, semver, rich, pympler, pydeck, gitpython, blinker, streamlit\n",
            "Successfully installed blinker-1.5 commonmark-0.9.1 gitdb-4.0.10 gitpython-3.1.29 pydeck-0.8.0 pympler-1.0.1 rich-12.6.0 semver-2.13.0 smmap-5.0.0 streamlit-1.15.2 validators-0.20.0 watchdog-2.2.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from numpy.core.multiarray import result_type\n",
        "import streamlit as st\n",
        "import pickle\n",
        "import string\n",
        "from nltk.corpus import stopwords\n",
        "import nltk\n",
        "from nltk.stem.porter import PorterStemmer\n",
        "ps = PorterStemmer()\n",
        "\n",
        "def transform_text(text):\n",
        "  text = text.lower()\n",
        "  text = nltk.word_tokenize(text)\n",
        "  y = []\n",
        "  for i in text:\n",
        "    if i.isalnum():\n",
        "       y.append(i)\n",
        "\n",
        "  text = y[:]\n",
        "  y.clear()\n",
        "  for i in text:\n",
        "    if i not in stopwords.words('english') and i not in string.punctuation:\n",
        "      y.append(i)\n",
        "  text = y[:]\n",
        "  y.clear()\n",
        "  for i in text:\n",
        "    y.append(ps.stem(i))\n",
        "  return \" \".join(y)\n",
        "\n",
        "tfidf = pickle.load(open('/content/vectorizer.pkl', 'rb'))\n",
        "model = pickle.load(open('/content/model.pkl', 'rb'))\n",
        "\n",
        "st.title(\"Email/SMS Spam Classifier\")\n",
        "input_message = st.text_area(\"Enter the message\")\n",
        "if st.button(\"Predict\"):\n",
        "  # 1. preprocess\n",
        "  transformed_sms = transform_text(input_message)\n",
        "  # 2. vectorize\n",
        "  vector_input = tfidf.transform([transformed_sms])\n",
        "  # 3. Predict\n",
        "  result = model.predict(vector_input)[0]\n",
        "  # 4. Displacy\n",
        "  if result == 1:\n",
        "    st.header(\"Spam\")\n",
        "  else:\n",
        "    st.header(\"Not Spam\")\n",
        "\n",
        "  "
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "jmuSjxTLn-RB",
        "outputId": "f1a32606-0da4-4cff-fd5e-5177a81b398d"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "WARNING:root:\n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.8/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n",
            "2022-12-12 19:12:46.744 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.8/dist-packages/ipykernel_launcher.py [ARGUMENTS]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "fxSzgpaCwY_u"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}