# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    make_report.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: kferterb <kferterb@student.21-school.ru    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/09/18 16:14:05 by kferterb          #+#    #+#              #
#    Updated: 2022/09/19 09:53:51 by kferterb         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from analytics import Research
from config import parameters, report

def make_report():
    file, num_of_steps = parameters()
    research = Research(file)
    analytics = research.Analytics(research.file_reader())
    observation = analytics.counts()
    frac_check = analytics.fractions(observation)
    forecast_list = analytics.predict_random(num_of_steps)
    forecast = analytics.calc_random(forecast_list)
    result = report(observation, frac_check, num_of_steps, forecast)
    analytics.save_file(result, "report", "txt")

if __name__ == '__main__':
    make_report()
