{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "USD\n",
      "CNY\n",
      "1.0\n",
      "6.52615\n",
      "test_passed\n",
      "test_passed\n",
      "all_text_passes\n"
     ]
    }
   ],
   "source": [
    "currency_from=input()\n",
    "currency_to=input()\n",
    "amount_from=input()\n",
    "def exchange(currency_from, currency_to, amount_from):\n",
    "    '''In this exchange, the user can change money with the amount of 'amount_from' in curency 'currency_from' to the currency 'currency_to'.\\\n",
    "    The value returned represents the amount of money in currency 'currency_to' and has the type float.\\\n",
    "    'currency_from' and 'currency_to' must be a three-letter(capital) string ; 'amount_from' should be a float.''' \n",
    "    from urllib.request import urlopen\n",
    "    \n",
    "    doc = urlopen('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from))\n",
    "    docstr = doc.read()\n",
    "    doc.close()\n",
    "    jstr = docstr.decode('ascii')\n",
    "    L1=jstr.split('\"')\n",
    "    L2=(L1[7]).split(' ')\n",
    "    return(float(L2[0]))    \n",
    "print(exchange(currency_from, currency_to, amount_from))\n",
    "def test_exchange():\n",
    "    E1=exchange('USD','EUR',1.0)\n",
    "    E2=exchange('USD','CNY',1.0)\n",
    "    E3=exchange('USD','GBP',1.0)\n",
    "    assert(round(E1,3) == 0.838)\n",
    "    assert(round(E2,3) == 6.526)\n",
    "    assert(round(E3,3) == 0.766)\n",
    "    print('test_passed')\n",
    "test_exchange()     "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
